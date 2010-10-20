# -*- coding: utf-8 -*-
"""
Downpy

:author: Rogério Vicente
:license: See LICENSE file for details
"""

__version__ = '1.0'

import sys

if __name__ == '__main__':
	from downpy.cmdline import main
	sys.exit(main(sys.argv))
