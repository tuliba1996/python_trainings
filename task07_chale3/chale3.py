#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2     # use library urllib2
import re 			# ues library regular 
# send request to pythonchallenge.com, read file uequality.html
html = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
# find all character between '<!--*-->' 
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
# find all group matches pattern in data, and print 
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))



