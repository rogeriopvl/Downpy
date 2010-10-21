# -*- coding: utf-8 -*-

import sys, re, parser, extensions
from optparse import OptionParser
from urlparse import urljoin

def main(args=sys.argv):
	
	# lets build the command line parser
	usage = "usage: %prog [options] url"
	version = "Downpy v1.0"
	cmdParser = OptionParser(usage, version=version)
	
	cmdParser.add_option("-e", "--extension", help="Choose specific file extension. Only files with this extension will be downloaded.")
	cmdParser.add_option("-f", "--filetype", help="Choose a type of files to download: audio, video, doc.")
	cmdParser.add_option("-o", "--output", help="Choose the destination folder for your downloaded files")
	
	(options, args) = cmdParser.parse_args()

	if (len(args) != 1):
		cmdParser.error("missing web page url")
	
	if options.extension:
		extensions = ['.'+options.extension]
	elif options.filetype:
		if options.filetype == "audio":
			extensions = extensions.audio
		elif options.filetype == "video":
			extensions = extensions.video
		elif options.filetype == "doc":
			extensions = extensions.doc
		else:
			cmdParser.error("Error: wrong filetype")

	# point to the output options dir
	if options.output:
		try:
			os.chdir(options.output)
		except OSError:
			print "Output directory doesn't exist! Saving downloads to current directory."
	
	print "Downloading page in %s" % args[0]
	links = parser.parsePage(args[0], extensions)
	print "Done!"
	
	print "Page contains %d downloadable links." % len(links)

	# if there are links to download, create a folder
	if len(links) > 0:
		# the directory contains a timestamp to avoid conflicts
		folderName = "download_%d" % int(time.time())
		os.mkdir(folderName)
	
	for link in links:
		if not re.match('https?://.*',link):
			link = urljoin(args[0], link)
		print "Downloading %s" % link
		downloader.download(link, folderName)
	
	print "Downpy terminated."
