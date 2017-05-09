import utils
import sys


class Scraper():
    def __init__(self):
        if not utils.is_python3():
            print("Please run using Python 3")
            sys.exit(0)
        else:
            try:
                imp.find_module('eggs')
                found = True
            except ImportError:
                found = False

    def

    def run(self):



