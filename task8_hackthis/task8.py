f1 = open("data.txt", 'r').read();
f2 = open("wordlist.txt", 'r').read()

strdata = f1.split()
strsrc = f2.split()

result=[]
for i in strdata:
	line1 = list(i)
	line1.sort()
	for j in strsrc:
		line2 = list(j)
		line2.sort()
		if line1 == line2 :
			result.append(j)
str = ''
for k in result:
	str = str + k + ','
print str 

