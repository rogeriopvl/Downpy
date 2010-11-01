# -*- coding: utf-8 -*-

'''
File: queue.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Contributor: David Cruz <http://github.com/dcruz>
Description: Just a wrapper of a queue and all its operations.
A deque is being used has this data structure is more efficient when we append and pop only
from both ends.
'''

from collections import deque
import pickle

class UrlQueue(object):

	def __init__(self, items=[]):
		"""You can pass items or ignore it at your will"""
		self.items = deque(items)
	
	def add(self, url):
		"""Adds an url to the queue. If its a relative url, the base is added"""
		self.items.append(url)
	
	def next(self):
		"""Get the next element in the queue"""
		try:
			return self.items.popleft()
		except IndexError:
			return False
	
	def hasNext(self):
		return len(self.items) > 0

	def size(self):
		return len(self.items)

	def saveState(self, folderName):
		try:
			fd = open(folderName+'/download.dat', "w")
			pickle.dump(self.items, fd)
			fd.close()
			return True
		except:
			return False
	
	def recoverState(self, folderName):
		"""Opens a file with the download links and rebuilds the queue"""
		try:
			fd = open(folderName+'/download.dat', "r")
			self.items = deque(pickle.load(fd))
			fd.close()
			return True
		except:
			return False
