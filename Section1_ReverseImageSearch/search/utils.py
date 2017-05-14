import sys

def is_python3():
    """
    Checks if running Python3
    :return:  True if Python3 else False
    """
    if sys.version_info >= (3, 0):
        return True
    return False
