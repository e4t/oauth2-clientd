#!/usr/bin/python3
# vim: sw=4 ts=4 et si:
"""
Setup file for installation
"""

import sys

from setuptools import setup

setup(
    name="oauth2-clientd",
    version="0.7",
    python_requires='>=3.6',

    author="Jeff Mahoney",
    author_email="jeffm@suse.com",
    description = "OAUTH2 client that caches refresh tokens securely",
    install_requires=['requests-oauthlib', 'python-daemon', 'cryptography',
                      'atomicwrites'],
    packages = [ "oauth2_clientd", "oauth2_clientd.data" ],
    package_data={'oauth2_clientd': ['data/*.conf']},

    scripts=["scripts/oauth2-clientd"])
