import urllib2
import re

ul = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
pat = re.compile("and the next nothing is (\d+)")
number= str(16044/2)
while True :
	data = urllib2.urlopen(ul % number).read()
	print data
	reg = pat.search(data)
	if reg == None:
		break
	number = reg.group(1)





