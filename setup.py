#!/usr/bin/env python3
from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='menus',
    version='0.1.7',
    description='Easy menu tool for gathering inputs',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bensmithyx/menus.git',
    author='Ben Smith',
    author_email='ben.work.smith@gmail.com',
    license='GNU GPLv3',
    packages=["menus"],
    install_requires=[],


    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
