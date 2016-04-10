#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-static-autocollect',
    version='0.1',
    url='https://github.com/andreyrusanov/django-static-autocollect',
    license='BSD',
    description='Runs collectstatic automatically.',
    long_description=README,
    author='Andrey Rusanov',
    author_email='andrey@rusanov.me',
    packages=find_packages(),
    install_requires=[
        'Django >= 1.6',
        'watchdog == 0.8.3'
    ],
    requires=[
        'Django(>= 1.6)',
        'watchdog(== 0.8.3)'
    ],
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
