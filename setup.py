#!/usr/bin/python

import os

try:
    # this is primarily to support the 'develop' target
    # if setuptools/distribute are installed
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# include all links to urlsearch in scripts
scripts = []
for scriptname in os.listdir('scripts'):
    script = os.path.join('scripts', scriptname)
    try:
        if os.path.samefile(script, 'scripts/urlsearch'):
            scripts.append(script)
    except OSError:
        pass

setup(
    name="urlsearch",
    version="0.3",
    description="perform web searches from the command line",
    long_description=open('README.rst').read(),
    author="Ben Bass",
    author_email="benbass@codedstructure.net",
    url="http://bitbucket.org/codedstructure/urlsearch",
    packages=["urlsearch"],
    data_files=[(os.path.expanduser('~'), (".urlsearchrc", ))],
    scripts=scripts,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
