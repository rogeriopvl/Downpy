# -*- coding: utf-8 -*-

import urllib2

def parsePage(url, extensions):
		
	from beautifulsoup import BeautifulSoup as soup
	
	links = []
	htmlContent = urllib2.urlopen(url).read()
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
