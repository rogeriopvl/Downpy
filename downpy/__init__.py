#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
File: __init__.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Fires up the downpy command line
'''
__version__ = '1.2'

import sys

if __name__ == '__main__':
	from downpy.cmdline import main
	sys.exit(main(sys.argv))
