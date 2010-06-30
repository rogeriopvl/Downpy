#!/usr/local/env python
"""
DownPy.py

Copyright 2008 Rogerio Vicente

This script downloads a given HTML file and parses all links in it,
to download every file linked.

This script was made to be used along with Filebuster <http://rogeriopvl.com/filebuster>
"""
import urllib2
from optparse import OptionParser

def parsePage(url):

	audio_extensions = ['.mp3', '.ogg', '.mp4a', '.wma', '.aac']
	
	from BeautifulSoup import BeautifulSoup as soup
	
	links = []
	content = soup(urllib2.urlopen(url).read())
	
	for tag in content.findAll('a', {'href': True}):
		link = tag.attrMap['href']
		if True in [link.endswith(ex) for ex in audio_extensions]:
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
	"""main method"""
	usage = "usage: %prog [options] url"
	version = "Downpy v1.0"
	parser = OptionParser(usage, version=version)
	
	parser.add_option("-e", "--extension", help="Choose specific file extension. Only files with this extension will be downloaded.")
	
	(options, args) = parser.parse_args()
	
	if (len(args) != 1):
		parser.error("missing web page url")
	
	if options.extension:
		print "TODO"
		
	print "Downloading page in %s" % args[0]
	links = parsePage(args[0])
	print "Done!"
	
	print "Page contains %d downloadable links." % len(links)
	
	for link in links:
		print "Downloading %s" % link
		download(args[0]+"/"+link)
	
	print "Downpy terminated."

if __name__ == "__main__":
	main()
