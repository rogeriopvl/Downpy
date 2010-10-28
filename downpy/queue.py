# -*- coding: utf-8 -*-

'''
File: queue.py
Author: Rogerio Vicente <httt://rogeriopvl.com>
Description: Just a wrapper of a queue and all its operations.
A deque is being used has this data structure is more efficient when we append and pop only
from both ends.
'''

from collections import deque

class Queue(object):

	def __init__(self):
		self.items = deque()
	
	def add(self, url):
		self.items.append(url)
	
	def next(self):
		try:
			return self.items.popleft()
		except IndexError:
			return False
	
	def recover(self, serializedFile):
		self.items = deque(open(serializedFile))
