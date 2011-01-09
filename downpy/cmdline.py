# -*- coding: utf-8 -*-
'''
File: cmdline.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Contributors: David Cruz <http://github.com/dcruz>
Description: All the command lines interactions and output
'''
import sys, os
import urlqueue, downloader, parser, extensions
from downpy import __version__
from optparse import OptionParser

def main(args=sys.argv):
	
	# lets build the command line parser
	usage = "usage: %prog [options] url"
	version = "Downpy "+__version__
	cmdParser = OptionParser(usage, version=version)

	# default to audio files
	ftypes = extensions.audio

	# default search filter option
	searchFilter = None

	cmdParser.add_option("-e", "--extension", help="Choose specific file extension. Only files with this extension will be downloaded.")
	cmdParser.add_option("-f", "--filetype", help="Choose a type of files to download: audio, video, doc.")
	cmdParser.add_option("-s", "--search", help="Only download links that match contain this given string")
	cmdParser.add_option("-o", "--output", help="Choose the destination folder for your downloaded files")
	
	(options, args) = cmdParser.parse_args()

	if (len(args) != 1):
		cmdParser.error("missing web page url")

	if options.search:
		searchFilter = options.search
	
	if options.extension:
		ftypes = ['.'+options.extension]
	elif options.filetype:
		if options.filetype == "audio":
			ftypes = extensions.audio
		elif options.filetype == "video":
			ftypes = extensions.video
		elif options.filetype == "doc":
			ftypes = extensions.doc
		else:
			cmdParser.error("wrong filetype")

	# point to the output options dir
	if options.output:
		try:
			os.chdir(options.output)
		except OSError:
			print "Info: output directory doesn't exist! Saving downloads to current directory."
	
	# get the folder name from the url
	folderName = parser.parseFolderName(args[0])

	# check if the download folder already exists
	if os.path.exists(folderName):
		print "Found incomplete download. Resuming..."
		queue = urlqueue.UrlQueue()
		queue.recoverState(folderName)
	else:
		print "Downloading page in %s" % args[0]
		queue = urlqueue.UrlQueue(parser.parsePage(args[0], ftypes, searchFilter))
		print "Done!"
		print "Page contains %d downloadable links." % queue.size()

		# if there are links to download, create a folder
		if queue.size() > 0:
			try:
				os.mkdir(folderName)
				queue.saveState(folderName)
			except OSError:
				print "Info: download folder already exists, overwriting..." 
	
	dl = downloader.Downloader(folderName)
	while queue.hasNext():
		link = queue.next()
		dl.download(link)
		queue.saveState(folderName)
	
	print "Downpy terminated."
