# -*- coding: utf-8 -*-
'''
File: downloader.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Module for functions related to file downloading
'''
import urllib2
import parser

def downloadFile(url, folder):
	"""Dowloads files from urls"""
	try:
		res = urllib2.urlopen(url)
	except:
		print "Error: invalid url"
		exit()
	try:
		f = open(folder+"/"+parser.parseFilename(url), "wb")
		for line in res:
			f.write(line)
		f.close()
	except IOError:
		print "Error: error saving file"
		exit()

