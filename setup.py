#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages # type: ignore[import-untyped]

setup(
    name = 'parsec',
    version = '3.17',
    description = 'parser combinator.',
    long_description = 'A universal Python parser combinator library inspired by Parsec library of Haskell.',
    author = 'He Tao',
    author_email = 'sighingnow@gmail.com',
    url = 'https://github.com/sighingnow/parsec.py',
    license = 'MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Compilers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
    ],
    platforms = 'any',
    keywords = 'monad parser combinator',

    install_requires = [
        'enum34; python_version < "3.5"',
        'setuptools',
    ],
    extras_require={
        'dev': [
            'mypy ~= 1.15.0',
            'coverage',
        ],
    },
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    package_data = {'': ('py.typed', '*.pyi')},

    test_suite = 'parsec.tests',

    project_urls={
        'Documentation': 'https://pythonhosted.org/parsec/',
        'Source': 'https://github.com/sighingnow/parsec.py',
        'Tracker': 'https://github.com/sighingnow/parsec.py/issues',
    },
)
