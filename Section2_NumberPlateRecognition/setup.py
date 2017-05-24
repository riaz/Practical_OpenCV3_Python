import os
from setuptools import setup


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Recee",
    version="0.1.0",
    author="Riaz Munshi",
    author_email="riaz.2012@gmail.com",
    description=("Finding Targets and Number Plate Recognition in Drone Video Streams"),
    keywords="opencv3 vision ocr cars number plate python3",
    packages=['drone'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Topic :: Number Plate Recognition"
    ]
)
