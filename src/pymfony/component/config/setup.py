#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is part of the pymfony package.
#
# (c) Alexandre Quercia <alquerci@email.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
from __future__ import absolute_import;

import os;
from distutils.core import setup;

"""
"""

realpathfile = os.path.realpath(os.path.dirname(__file__));
os.chdir(realpathfile);

f = open("README.md");
long_description = "\n"+f.read();
f.close();

def find_packages():
    return [
        'pymfony.component.config',
    ];

def find_package_data():
    return {
    };

setup(
    name="pymfony.yaml",
    version="2.2.0b1",
    package_dir={'pymfony.component.config': ''},
    packages=find_packages(),
    package_data=find_package_data(),
    author="Alexandre Quercia",
    author_email="alquerci@email.com",
    url="http://github.com/alquerci/pymfony-config",
    description='Pymfony Config Component',
    long_description=long_description,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
);
