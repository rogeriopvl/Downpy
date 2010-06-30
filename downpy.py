#!/usr/local/env python
"""
DownPy.py

Copyright 2008 Rogerio Vicente

This script downloads a given HTML file and parses all links in it,
to download every file linked.

This script was made to be used along with Filebuster <http://rogeriopvl.com/filebuster>
"""
import urllib2
import os
from optparse import OptionParser

def parsePage(url, extensions):
		
	from BeautifulSoup import BeautifulSoup as soup
	
	links = []
	content = soup(urllib2.urlopen(url).read())
	
	for tag in content.findAll('a', {'href': True}):
		link = tag.attrMap['href']
		# gotta love this
		if True in [link.endswith(ex) for ex in extensions]:
			links.append(link)
		
	return links
	
def download(furl):
	try:
		res = urllib2.urlopen(furl)
		f = open(parseFilename(furl), "wb")
		for line in res:
			f.write(line)
		f.close()
	except:
		print "Error: invalid url"
		exit()

def parseFilename(link):
	pieces = link.split('/')
	
	return pieces[len(pieces)-1].replace("%20", " ")

def main():
	"""main method: its too big... think about it"""
	
	# default extensions, these should become something like constants
	audioExtensions = ['.mp3', '.ogg', '.mp4a', '.wma', '.aac']
	videoExtensions = ['.avi', '.mp4', '.wmv', '.flv']
	docExtensions = ['.doc', '.docx', '.txt', '.rtf', '.pdf', '.epub', '.chm']
	
	# lets build the command line parser
	usage = "usage: %prog [options] url"
	version = "Downpy v1.0"
	parser = OptionParser(usage, version=version)
	
	parser.add_option("-e", "--extension", help="Choose specific file extension. Only files with this extension will be downloaded.")
	parser.add_option("-f", "--filetype", help="Choose a type of files to download: audio, video, doc.")
	
	(options, args) = parser.parse_args()
	
	# default extensions
	extensions = audioExtensions
	
	# define the behavior according to the passed arguments
	if (len(args) != 1):
		parser.error("missing web page url")
	
	if options.extension:
		extensions = [options.extension]
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
	print "Downloading page in %s" % args[0]
	links = parsePage(args[0], extensions)
	print "Done!"
	
	print "Page contains %d downloadable links." % len(links)
	
	for link in links:
		print "Downloading %s" % link
		download(args[0]+"/"+link)
	
	print "Downpy terminated."

if __name__ == "__main__":
	main()
