# -*- coding: utf-8 -*-
"""CI 入口（`.github/workflows/check-images.yml`）：复用 tools/check_images.py。

报告固定写仓库根 `image-report.md`，供工作流判断存在性后开 issue；
检查逻辑、口径与退出码见 tools/check_images.py 的 docstring。
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from tools.check_images import main  # noqa: E402

if __name__ == '__main__':
    sys.exit(main(['--root', ROOT, '--out', os.path.join(ROOT, 'image-report.md')]))
