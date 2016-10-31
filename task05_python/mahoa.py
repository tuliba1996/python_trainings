
f= open("cipher.txt", 'r')
str = f.read()

key = 14
for i in str:
	if i.isalpha():
		a=''
		a = ord(i) + key
		if (a > 90) & (a < 97):
				a = a + 6
		if a>122:
			a = a-58		
		b = chr(a)
		print b