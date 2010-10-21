# -*- coding: utf-8 -*-

import urllib2
import parser

"""Dowloads files from urls"""
def downloadFile(url, folder):
	try:
		res = urllib2.urlopen(url)
		f = open(folder+"/"+parser.parseFilename(url), "wb")
		for line in res:
			f.write(line)
		f.close()
	except:
		print "Error: invalid url"
		exit()
