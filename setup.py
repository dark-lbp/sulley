#!/usr/bin/env python
# -*- coding: utf-8 -*-

PROJECT = 'Sulley'
VERSION = '1.0.0'

# Bootstrap installation of Distribute
try:
    from setuptools import setup, find_packages
except ImportError, m:
    print "[-] Error: ".format(m)

setup(
    name=PROJECT,
    version=VERSION,
    author='Pedram Amini, Aaron Portnoy, Ryan Sears',
    author_email='pedram.amini@gmail.com, aportnoy@gmail.com, fitblip@gmail.com',
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
        'Sulley Fuzzing Framework.'
    ),
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['docs', 'examples', 'installer']),
    include_package_data=True,
)
