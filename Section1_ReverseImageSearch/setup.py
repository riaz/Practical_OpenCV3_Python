import os
from setuptools import setup


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Canvas",
    version="0.1.0",
    author="Riaz Munshi",
    author_email="riaz.2012@gmail.com",
    description=("Reverse Image Search Engine built using Python3, OpenCV3 and lots of Love <} "),
    keywords="opencv3 vision search python3",
    packages=['search'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Search Engine"
    ]
)
