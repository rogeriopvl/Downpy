# -*- coding: utf-8 -*-

import urllib2

"""Dowloads files from urls"""
def downloadFile(self, url):
	try:
		res = urllib2.urlopen(furl)
		f = open(folder+"/"+self.parseFilename(furl), "wb")
		for line in res:
			f.write(line)
		f.close()
	except:
		print "Error: invalid url"
		exit()
