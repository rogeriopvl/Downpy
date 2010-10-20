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
		entry_points = { 'console_scripts': ['downpy = downpy.cmdline:main'], }
	)
else:
	add_keywords = dict(
		scripts = ['downpy']
	)

setup (
	name = "Downpy",
	packages = ["downpy"],
	version = "1.0",
	description =  "Downloads all files from a web page.",
	author = "Rogerio Vicente",
	author_email = "rogeriopvl@gmail.com"
	url = "http://github.com/rogeriopvl/downpy",
	download_url = "",
	keywords = "",
	platforms = 'any',
	zip_safe = False,
	include_package_data = True,
	classifiers = [],
	long_description = "",
	cmdclass = {'build_py': build_py},
	**add_keywords
)
