# usr/bin/python -tt
import re
import zipfile

f = zipfile.ZipFile('channel.zip')
num = '90052'

result = ''

while True:
	data = f.read(num + '.txt')
	result += f.getinfo(num + '.txt').comment
	print data
	cmp = re.search("Next nothing is (\d+)", data)   
	if cmp == None:
	    	break
    	num = cmp.group(1)
print result
