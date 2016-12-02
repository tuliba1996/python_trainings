
a = ['1']
def addnum (a):
	count = 0
	stt = ''
	block = a[0]
	for i in a:
		if i == block:
			count += 1;
		else:
			stt += str(count) + block 
			block = i
			count =1
	stt += str(count) + block 
	return stt;
j=0
for i in a:
	j += 1
	if (j<31):
		b = addnum(i)
		a.append(b)
print len(a[30]) 
 