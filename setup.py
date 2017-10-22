"""This file contains necessary setup files."""

from setuptools import setup

setup(
    name='Codewars Katas',
    description='This module contains katas.',
    author='Matt',
    author_email='mattfavoino@gmail.com',
    package_dir={'': 'src'},
    py_modules=['die'],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']}
)
