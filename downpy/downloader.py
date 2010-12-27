# -*- coding: utf-8 -*-
'''
File: downloader.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Module for functions related to file downloading
'''
import urllib
import parser
import sys
from ui.progressbar import ProgressBar, TerminalController

class Downloader(object):

	def __init__(self, folder):
		self.folder = folder

	def download(self, url):
		"""Dowloads files from urls"""
		try:
			fname = parser.parseFileName(url)
			fname, headers = urllib.urlretrieve(url, self.folder+"/"+fname, reporthook=DownloadReporter(fname))
		except IOError:
			print "Error: error downloading/saving file"
			exit()

class DownloadReporter:

	def __init__(self, fname):
		try:
			self.ui = ProgressBar(TerminalController(sys.stdout), 'Downloading '+ fname)
		except ValueError:
			print 'ERROR UI'
			print 'Downloading', fname
			self.ui = None
	def __call__(self, blocks, block_size, total_size):
		percent = (blocks * block_size) / float(total_size)
		if self.ui is None:
			print 'Downloaded {0:%}'.format(percent)
		else:
			self.ui.update(percent)
