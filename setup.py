#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PROJECT = 'Sulley 3'
VERSION = '3.0.1'

# Bootstrap installation of Distribute
try:
    from setuptools import setup, find_packages
except ImportError:
    print("Import error: install setuptools first.")

setup(
    name=PROJECT,
    version=VERSION,
    author='Pedram Amini, Aaron Portnoy, Ryan Sears, Yannick Formaggio',
    author_email='pedram.amini@gmail.com, aportnoy@gmail.com, fitblip@gmail.com, yannick@thelumberjhack.org',
    url='https://github.com/yformaggio/sulley',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GPL V2',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    platforms=['Any'],
    description=(
        'Sulley Fuzzing Framework python 3 implementation.'
    ),
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['docs', 'examples', 'installer']),
    include_package_data=True,
)
