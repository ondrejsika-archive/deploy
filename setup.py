#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "deploy",
    version = "1.0.0",
    url = 'http://ondrejsika.com/docs/deploy',
    download_url = 'https://github.com/sikaondrej/deploy',
    license = 'GNU LGPL v.3',
    description = "Easy deploy Python WSGI apps",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    scripts = ["deploy/bin/deploy-startserver", ]
    install_requires = [],
    include_package_data = True,
)
