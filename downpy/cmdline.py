# -*- coding: utf-8 -*-

import sys
from optparse import OptionParser

def main(args=sys.argv):
	
	# lets build the command line parser
	usage = "usage: %prog [options] url"
	version = "Downpy v1.0"
	parser = OptionParser(usage, version=version)
	
	parser.add_option("-e", "--extension", help="Choose specific file extension. Only files with this extension will be downloaded.")
	parser.add_option("-f", "--filetype", help="Choose a type of files to download: audio, video, doc.")
	parser.add_option("-o", "--output", help="Choose the destination folder for your downloaded files")
	
	(options, args) = parser.parse_args()
