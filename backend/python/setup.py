#!/usr/bin/python2.7
import sys
from setuptools import setup, find_packages

setup(
    name='addressbook',
    version='0.0.1',
    packages=find_packages(exclude=('tests','sql', 'conf', 'doc',)),
    py_modules=[''],
    author='Enrique Ojeda Lara',
    author_email='enriqueojedalara@gmail.com',
    description='Address book example using python/tornado/mysql (Just server side using RESTful services)',
    keywords='AddressBook',
    test_suite='unittests',
)
