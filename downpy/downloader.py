# -*- coding: utf-8 -*-
'''
File: downloader.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Module for functions related to file downloading
'''
import urllib2
import parser

class Downloader(object):

	def __init__(self, folder):
		self.folder = folder

	def download(self, url):
		"""Dowloads files from urls"""
		try:
			res = urllib2.urlopen(url)
		except:
			print "Error: invalid url"
			exit()
		try:
			f = open(self.folder+"/"+parser.parseFileName(url), "wb")
			for line in res:
				f.write(line)
			f.close()
		except IOError:
			print "Error: error saving file"
			exit()

