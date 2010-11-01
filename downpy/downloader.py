# -*- coding: utf-8 -*-
'''
File: downloader.py
Author: Rogerio Vicente <http://rogeriopvl.com>
Description: Module for functions related to file downloading
'''
import urllib
import parser

def downloadFile(url, folder):
    """Dowloads files from urls"""
    try:
        fname, headers = urllib.urlretrieve(url, folder+"/"+parser.parseFilename(url))
    except:
        print "Error: invalid url"
        exit()
