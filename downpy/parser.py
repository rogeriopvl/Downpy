# -*- coding: utf-8 -*-
'''
File: parser.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Contains the parsing functions needed to parse the html page for links
and the filename from the url
'''
import urllib2, re
from urlparse import urljoin

def parsePage(url, extensions):
	"""Parses a given webpage and fetches all link sources"""
	from beautifulsoup import BeautifulSoup as soup
	
	links = []
	try:
		htmlContent = urllib2.urlopen(url).read()
	except:
		print "Error: can't open url"
		exit()
	
	content = soup.BeautifulSoup(htmlContent)

	# get all hrefs and srcs in the page
	results = content.findAll('a', {'href': True})
	results.extend(content.findAll(attrs={'src': True}))

	for tag in results:
		link = tag['href']
		# pythonic perfection ahead!
		if True in [link.endswith(ex) for ex in extensions]:
			if not re.match('https?://.*',link):
				link = urljoin(url, link)
			links.append(link)	
	return links

def parseFileName(url):
	"""Parses the file name from a given url"""
	pieces = url.split('/')
	return pieces[len(pieces)-1].replace("%20", " ")

def parseFolderName(url):
	"""Parses the folder name from a given url"""
	pieces = url.split('/')
	pieces = [s for s in pieces if s] # remove all empty strings

	if '.' in pieces[len(pieces)-1]:
		folderName = pieces[len(pieces)-2].replace("%20", "_")
	else:
		folderName = pieces[len(pieces)-1].replace("%20", "_")

	if ':' in folderName:
		return pieces[len(pieces)-1]
	else:
		return folderName
