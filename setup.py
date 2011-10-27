#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='aps',
    version='0.1',
    description='Script to setup arduino project',
    author='Diego Rubin',
    author_email='rubin.diego@gmail.com',
    url='http://diegorubin.com/aps',

    include_package_data = True,
    package_data = {
        'aps': ['data/Makefile.arduino',
                'data/template.pde'],
    },

    packages=find_packages()
)
