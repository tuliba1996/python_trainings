from PIL import Image
import re


im = Image.open("oxygen.png")
width = im.size[0]
height = im.size[1]/2
result = ''
for i in range(1,width,7):
	li = im.getpixel((i,height))
	result += chr(li[0])
ser = re.findall('\[(.*)\]', result)[0].split(', ')
out = ''
for j in ser:
	tk = int(j)
	out += chr(tk)
print out


