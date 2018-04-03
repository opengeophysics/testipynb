#!/usr/bin/env python
from __future__ import print_function
"""nbtest

unittest a collection of jupyter notebooks
"""

from distutils.core import setup
from setuptools import find_packages


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Physics',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS',
    'Natural Language :: English',
]

with open('README.rst') as f:
    LONG_DESCRIPTION = ''.join(f.readlines())

setup(
    name = 'nbtest',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'future',
        'numpy>=1.7',
        'ipywidgets',
        'jupyter',
        'nbconvert',
        'nbformat',
    ],
    author = 'Lindsey Heagy',
    author_email = 'lindseyheagy@gmail.com',
    description = 'nbtest',
    long_description = LONG_DESCRIPTION,
    keywords = 'jupyter, testing',
    url = 'http://github.com/lheagy/nbtest',
    download_url = 'http://github.com/lheagy/nbtest',
    classifiers=CLASSIFIERS,
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    license='MIT License',
    use_2to3 = False,
)
