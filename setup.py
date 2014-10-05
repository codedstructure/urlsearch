#!/usr/bin/python

try:
    # this is primarily to support the 'develop' target
    # if setuptools/distribute are installed
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="urlsearch",
    version="0.1",
    description="perform web searches from the command line",
    long_description=open('README.rst').read(),
    author="Ben Bass",
    author_email="benbass@codedstructure.net",
    url="http://bitbucket.org/codedstructure/xmlcmd",
    packages=["urlsearch"],
    scripts=['scripts/urlsearch'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python" ,
        "Programming Language :: Python :: 2.7" ,
        "Programming Language :: Python :: 3",
    ]
)
