# -*- coding: utf-8 -*-
'''
File: parser.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Contains the parsing functions needed to parse the html page for links
and the filename from the url
'''
import sys, urllib2

def parsePage(url, extensions):
		
	from beautifulsoup import BeautifulSoup as soup
	
	links = []
	try:
		htmlContent = urllib2.urlopen(url).read()
	except:
		print "Error: can't open url"
		sys.exit()
	
	content = soup.BeautifulSoup(htmlContent)

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


def parseFilename(url):
	try:
		pieces = url.split('/')
		return pieces[len(pieces)-1].replace("%20", " ")
	except:
		print "Error: parsing error for ["+ url +"]"
