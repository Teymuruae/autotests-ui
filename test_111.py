import platform
import sys

from config import settings


def test_1():
    print('=' *50)
    print(sys.version)
    print(platform.platform(), platform.version())

# os_info=Darwin, 22.6.0
# python_version=3.11.9 (main, Apr 2 2024, 08:25:04) [Clang 15.0.0 (clang-1500.1.0.2.5)]

