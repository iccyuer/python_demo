# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="app",
    version="1.0",
    author="tutu",
    description="描述信息",
    platforms='python3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'redis'
    ]
)