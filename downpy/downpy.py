#!/usr/bin/env python
"""
downpy.py

Copyright 2008 Rogerio Vicente

This script downloads a given HTML file and parses all links in it,
to download every file linked.

This script was made to be used along with Filebuster <http://rogeriopvl.com/filebuster>
"""
import urllib2
import os, time
import re
from optparse import OptionParser
from urlparse import urljoin

def parsePage(url, extensions):
		
	from BeautifulSoup import BeautifulSoup as soup
	
	links = []
	content = soup(urllib2.urlopen(url).read())

	for tag in content.findAll('a', {'href': True}):
		link = tag['href']
		# gotta love this
		if True in [link.endswith(ex) for ex in extensions]:
			links.append(link)

	for tag in content.findAll(attrs={'src': True}):
		link = tag['src']
		if True in [link.endswith(ex) for ex in extensions]:
			links.append(link)
	return links
	
def download(furl, folder):
	try:
		res = urllib2.urlopen(furl)
		f = open(folder+"/"+parseFilename(furl), "wb")
		for line in res:
			f.write(line)
		f.close()
	except:
		print "Error: invalid url"
		exit()

def parseFilename(link):
	try:
		pieces = link.split('/')
		return pieces[len(pieces)-1].replace("%20", " ")
	except:
		print "Error: parsing error for ["+ link +"]"

def main():
	"""main method: its too big... think about it"""
	
	# some filetypes are incomplete but this should do it for now
	audioExtensions = ['.mp3', '.oga', '.ogg', '.mp4a', '.wma', '.aac', '.mid']
	videoExtensions = ['.avi', '.flv', '.mp4', '.mkv', '.ogv', '.webm', '.wmv']
	docExtensions = ['.chm', '.doc', '.docx', '.epub', '.mobi', '.odf', '.pdf', '.rtf', '.txt']
	
	# lets build the command line parser
	usage = "usage: %prog [options] url"
	version = "Downpy v1.0"
	parser = OptionParser(usage, version=version)
	
	parser.add_option("-e", "--extension", help="Choose specific file extension. Only files with this extension will be downloaded.")
	parser.add_option("-f", "--filetype", help="Choose a type of files to download: audio, video, doc.")
	parser.add_option("-o", "--output", help="Choose the destination folder for your downloaded files")
	
	(options, args) = parser.parse_args()
	
	# default extensions
	extensions = audioExtensions
	
	# define the behavior according to the passed arguments
	if (len(args) != 1):
		parser.error("missing web page url")
	
	if options.extension:
		extensions = ['.'+options.extension]
	elif options.filetype:
		if options.filetype == "audio":
			extensions = audioExtensions
		elif options.filetype == "video":
			extensions = videoExtensions
		elif options.filetype == "doc":
			extensions = docExtensions
		else:
			parser.error("Error: wrong filetype")
	
	# let the action begin

	# point to the output options' dir
	if options.output:
		try:
			os.chdir(options.output)
		except OSError:
			print "Output directory doesn't exist! Saving downloads to current directory."
	
	print "Downloading page in %s" % args[0]
	links = parsePage(args[0], extensions)
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
		download(link, folderName)
	
	print "Downpy terminated."

if __name__ == "__main__":
	main()
