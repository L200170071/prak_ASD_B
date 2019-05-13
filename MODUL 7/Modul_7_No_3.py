import re

#No 3
f = open('indonesia.txt', 'r', encoding='latin1')
teks = f.read()
f.close()
p = r'\s(di\s\w+)'
cocok = re.findall(p, teks)
