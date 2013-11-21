#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "deploy",
    version = "1.7.0",
    url = 'http://ondrejsika.com/docs/deploy',
    download_url = 'https://github.com/sikaondrej/deploy',
    license = 'MIT',
    description = "Easy deploy Python WSGI apps",
    author = 'Ondrej Sika',
    author_email = 'dev@ondrejsika.com',
    packages = find_packages(),
    scripts = [
        "deploy/bin/deploy",
        "deploy/bin/deploy-startserver",
        "deploy/bin/deploy-serverconf",
        "deploy/bin/deploy-init",
        "deploy/bin/deploy-restart",
        "deploy/bin/deploy-remove",
    ],
    install_requires = ["pip", "pycoffee"],
)
