"""deploy_bump.py 单测：临时建两个 git 仓库（SEP 仓 + 壳仓），用 gitlink 模拟子模块。"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(os.path.dirname(HERE), 'deploy_bump.py')


def git(cwd, *args, check=True):
    r = subprocess.run(['git', *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise AssertionError('git %s 失败：%s%s' % (' '.join(args), r.stdout, r.stderr))
    return r.stdout.strip()


class DeployBumpTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name
        self.sep = os.path.join(self.root, 'sep')
        self.shell = os.path.join(self.root, 'shell')
        os.makedirs(os.path.join(self.sep, 'tools'))
        shutil.copy(SCRIPT, os.path.join(self.sep, 'tools', 'deploy_bump.py'))
        self._init_repo(self.sep)
        self._init_repo(self.shell)
        # SEP 仓两个提交，target = 第二个
        self.write(self.sep, 'a.md', '# a\n')
        self.c1 = self.commit_all(self.sep, '首个提交')
        self.write(self.sep, 'a.md', '# a2\n')
        self.c2 = self.commit_all(self.sep, '第二个提交')
        # 壳仓先把 docs 指向 c1
        git(self.shell, 'update-index', '--add', '--cacheinfo', '160000,%s,docs' % self.c1)
        self.commit(self.shell, '初始指针')

    def tearDown(self):
        self._tmp.cleanup()

    def _init_repo(self, path):
        os.makedirs(path, exist_ok=True)
        git(path, 'init', '-q', '-b', 'main')
        git(path, 'config', 'user.name', 'test')
        git(path, 'config', 'user.email', 'test@example.com')

    def write(self, repo, rel, text):
        with open(os.path.join(repo, rel), 'w', encoding='utf-8', newline='') as f:
            f.write(text)

    def commit(self, repo, msg):
        """提交已暂存内容；`all=True` 时先 `add -A`。

        壳仓的 `docs` 是 gitlink（工作树里没有普通文件/目录时），`add -A` 会把它
        当删除从索引里抹掉——初始指针提交必须只提交已暂存的 cacheinfo。
        """
        git(repo, 'commit', '-q', '-m', msg)
        return git(repo, 'rev-parse', 'HEAD')

    def commit_all(self, repo, msg):
        git(repo, 'add', '-A')
        return self.commit(repo, msg)

    def bump(self, *extra, ref=None):
        return subprocess.run(
            [sys.executable, os.path.join(self.sep, 'tools', 'deploy_bump.py'),
             '--shell', self.shell, '--ref', ref or self.c2, '--no-push', *extra],
            capture_output=True, text=True,
        )

    def pointer(self):
        out = git(self.shell, 'ls-tree', 'HEAD', '--', 'docs')
        return out.split()[2] if out else None

    def test_bumps_pointer_and_is_idempotent(self):
        r = self.bump()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.pointer(), self.c2)
        self.assertIn('docs 指针前移', git(self.shell, 'log', '-1', '--format=%s'))
        n = len(git(self.shell, 'rev-list', 'HEAD').splitlines())
        r2 = self.bump()
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)
        self.assertIn('已是最新', r2.stdout)
        self.assertEqual(len(git(self.shell, 'rev-list', 'HEAD').splitlines()), n, '幂等：不应新增提交')

    def test_dry_run_changes_nothing(self):
        r = self.bump('--dry-run')
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.pointer(), self.c1)
        self.assertIn('[dry-run]', r.stdout)

    def test_refuses_target_not_on_origin(self):
        """指针指向未推送提交 → 壳仓 CI 取不到对象，必须拒绝。"""
        bare = os.path.join(self.root, 'sep-origin.git')
        git(self.root, 'init', '--bare', '-q', bare)
        git(self.sep, 'remote', 'add', 'origin', bare)
        git(self.sep, 'push', '-q', '-u', 'origin', 'main')
        git(self.sep, 'fetch', '-q', 'origin')
        self.write(self.sep, 'a.md', '# a3\n')
        c3 = self.commit_all(self.sep, '未推送的提交')
        r = self.bump(ref=c3)
        self.assertEqual(r.returncode, 1)
        self.assertIn('不在 origin/main 上', r.stdout)
        self.assertEqual(self.pointer(), self.c1)
        # 显式 --force 才放行
        r2 = self.bump('--force', ref=c3)
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)
        self.assertEqual(self.pointer(), c3)

    def test_refuses_other_dirty_files(self):
        self.write(self.shell, 'other.txt', 'x\n')
        r = self.bump()
        self.assertEqual(r.returncode, 1)
        self.assertEqual(self.pointer(), self.c1)

    def test_allow_dirty_commits_only_docs(self):
        self.write(self.shell, 'other.txt', 'x\n')
        git(self.shell, 'add', 'other.txt')
        git(self.shell, 'commit', '-q', '-m', '无关提交')
        self.write(self.shell, 'other.txt', 'y\n')
        r = self.bump('--allow-dirty')
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.pointer(), self.c2)
        self.assertEqual(git(self.shell, 'show', '--name-only', '--format=', 'HEAD'), 'docs')
        self.assertIn('other.txt', git(self.shell, 'status', '--porcelain'), '无关改动应仍留在工作区')


if __name__ == '__main__':
    unittest.main()
