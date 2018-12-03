#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Piotr Senkow",
    author_email='piotrsenkow@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="This is a test to see if I can put up a function python package. ",
    entry_points={
        'console_scripts': [
            'ficobois=ficobois.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ficobois',
    name='ficobois',
    packages=find_packages(include=['ficobois']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/piotrsenkow/ficobois',
    version='0.1.5',
    zip_safe=False,
)
