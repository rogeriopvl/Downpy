#!/usr/local/env python
"""
DownPy.py

Copyright 2008 Rogerio Vicente

This script downloads a given HTML file and parses all links in it,
to download every file linked.

This script was made to be used along with Filebuster <http://rogeriopvl.com/filebuster>
"""
import urllib2

def parse_page(url):

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
	res = urllib2.urlopen(furl)
	f = open(parse_filename(furl), "wb")
	for line in res:
		f.write(line)
	f.close()

def parse_filename(link):
	pieces = link.split('/')
	
	return pieces[len(pieces)-1].replace("%20", " ")

def display_help():
	print "Options:"
	print "-e: Let's you choose the file extension. Only files with this extension will be downloaded."

if __name__ == "__main__":
	
	import sys
	
	if len(sys.argv) != 2 and len(sys.argv) != 4:
		print "Usage: %s <website_url> [-e <file_extension>]" % sys.argv[0]
		print "Use -h for more info."
	elif len(sys.argv) == 2:
		if sys.argv[1] == "-h":
			display_help()
		else:
			print "Downloading index page in %s" % sys.argv[1]
			links = parse_page(sys.argv[1])
			print "Done!"
		
			print "index page contains %d downloadable links!" % len(links)
		
			for link in links:
					print "Downloading %s" % link
					download(sys.argv[1]+"/"+link)
		
			print "DownPy terminated!"
	elif len(sys.argv) == 4:
		print "TODO: specified file extension"
	else:
		print "nothing"
			
