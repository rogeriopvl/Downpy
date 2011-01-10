#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	from setuptools import setup, find_packages
	has_setuptools = True
except ImportError:
	from distutils.core import setup

	def find_packages():
		return [downpy]
	has_setuptools = False

try:
	from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
	from distutils.command.build_py import build_py

if has_setuptools:
	add_keywords = dict(
		entry_points = { 'console_scripts': ['down = downpy.cmdline:main'], }
	)
else:
	add_keywords = dict(
		scripts = ['down']
	)

setup (
	name = 'Downpy',
    version = '1.2',
    url = 'http://github.com/rogeriopvl/Downpy',
    license = 'BSD License',
    author = 'Rogerio Vicente',
    author_email = 'rogeriopvl@gmail.com',
    description = 'Downpy is a command line tool that downloads all files of a certain media type in a webpage.',
    long_description = '',
    keywords = 'download files',
    packages = find_packages(),
    platforms = 'any',
    zip_safe = False,
    include_package_data = True,
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    cmdclass = {'build_py': build_py},
    **add_keywords
)
