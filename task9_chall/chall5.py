import pickle
import urllib2

f = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p",'rb')
result = ''
pick = pickle.load(f)
for i in pick:	
	for j,k in i:
		result = result + j*k
print result