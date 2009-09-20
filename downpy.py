#!/usr/local/env python
"""
DownPy.py

This script downloads a given HTML file and parses all links in it,
to download every file linked.

This script was made to be used along with Filebuster <http://rogeriopvl.com/filebuster>
"""
import urllib2

def getWebPage (url):

	from BeautifulSoup import BeautifulSoup as soup
	
	links = []
	content = soup(urllib2.urlopen(url).read())
	
	for tag in content.findAll('a', {'href': True}):
		links.append(tag.attrMap['href'])
		
	return links
	
def downloadFile (furl):
	res = urllib2.urlopen(furl)
	f = open(getFileName(furl), "wb")
	for line in res:
		f.write(line)
	f.close()

def filterLinks (links):
	for link in links[:]:
		if not link.endswith('.mp3') and not link.endswith('.wma') and not link.endswith('.ogg') and not link.endswith('.aac'):
			links.remove(link)
	return links

def getFileName (link):
	pieces = link.split('/')
	
	return pieces[len(pieces)-1].replace("%20", " ")
		 

if __name__ == "__main__":
	
	import sys
	
	if len(sys.argv) <= 1:
		print "Usage: %s <website_url>" % sys.argv[0]
	else:
		print "Downloading index page in %s" % sys.argv[1]
		links = filterLinks(getWebPage (sys.argv[1]))
		print "Done!"
		
		print "index page contains %d downloadable links!" % len(links)
		
		for link in links:
				print "Downloading %s" % link
				downloadFile(sys.argv[1]+"/"+link)
		
		print "DownPy terminated!"
