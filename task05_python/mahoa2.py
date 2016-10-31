from string import maketrans
import string

alp = list(string.ascii_lowercase)
ALP = list(string.ascii_uppercase)
intab = ''.join(alp+ALP)

def outab(key):
	a = map(lambda x: alp[(alp.index(x)+key)%26], alp)
	b = map(lambda x: ALP[(ALP.index(x)+key)%26], ALP)
	return ''.join(a+b)



if __name__ == '__main__':
	messg = open('cipher.txt','r').read()
	# Da biet key ma hoa
	key = 14
	print messg.translate(maketrans(intab, outab(key)))+'\n'
	
	# Khi chua biet key ma hoa
	'''
	for key in range(1, 25):
		print 'Key = %d'%key + ' ='*30
		print messg.translate(maketrans(intab, outab(key)))+'\n'
'''





