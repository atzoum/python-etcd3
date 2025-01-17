#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            re.sub('==', '>=', line) for line in reqs_file.readlines()
            if not re.match(r'(\s*#|-r)', line)
        ]


requirements = load_reqs('requirements/base.txt')
test_requirements = load_reqs('requirements/test.txt')

setup(
    name='etcd3-rs',
    version='0.13.0',
    description="Fork of https://github.com/kragniz/python-etcd3",
    long_description=readme + '\n\n' + history,
    author="Aris Tzoumas",
    author_email='atzoumas@rudderstack.com',
    url='https://github.com/atzoum/python-etcd3',
    packages=[
        'etcd3',
        'etcd3.etcdrpc',
    ],
    package_dir={
        'etcd3': 'etcd3',
        'etcd3.etcdrpc': 'etcd3/etcdrpc',
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='etcd3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
