import sys


def is_python3():
    if sys.version_info >= (3, 0):
        return True
    return False


