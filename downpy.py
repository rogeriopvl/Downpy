#!/usr/local/env python
"""
DownPy.py

Copyright 2008 Rogerio Vicente

This script downloads a given HTML file and parses all links in it,
to download every file linked.

This script was made to be used along with Filebuster <http://rogeriopvl.com/filebuster>
"""
import urllib2

def getWebPage (url):

	audio_extensions = ['.mp3', '.ogg', '.mp4a', '.wma', '.aac']
	
	from BeautifulSoup import BeautifulSoup as soup
	
	links = []
	content = soup(urllib2.urlopen(url).read())
	
	for tag in content.findAll('a', {'href': True}):
		link = tag.attrMap['href']
		if True in [link.endswith(ex) for ex in audio_extensions]:
			links.append(link)
		
	return links
	
def downloadFile (furl):
	res = urllib2.urlopen(furl)
	f = open(getFileName(furl), "wb")
	for line in res:
		f.write(line)
	f.close()

def getFileName (link):
	pieces = link.split('/')
	
	return pieces[len(pieces)-1].replace("%20", " ")
		 

if __name__ == "__main__":
	
	import sys
	
	if len(sys.argv) <= 1:
		print "Usage: %s <website_url>" % sys.argv[0]
	else:
		print "Downloading index page in %s" % sys.argv[1]
		links = getWebPage (sys.argv[1])
		print "Done!"
		
		print "index page contains %d downloadable links!" % len(links)
		
		for link in links:
				print "Downloading %s" % link
				downloadFile(sys.argv[1]+"/"+link)
		
		print "DownPy terminated!"
