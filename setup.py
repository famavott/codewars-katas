"""This file contains necessary setup files."""

from setuptools import setup

setup(
    name='Mailroom Madness',
    description='This module contains functions, which trigger prompts, meant for command line execution.',
    author='Carson and Matt',
    author_email='carson.newton@outlook.com',
    package_dir={'': 'src'},
    py_modules=['mailroom'],
    install_requires=['ipython'],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox']},
    entry_points={
    }
)
