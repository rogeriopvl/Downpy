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
	name = "Downpy",
	platforms = 'any',
	zip_safe = False,
	include_package_data = True,
	classifiers = [],
	long_description = "",
	cmdclass = {'build_py': build_py},
	**add_keywords
)
