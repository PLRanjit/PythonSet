import re
f = open('SEATlIST.txt')
s = f.read()
k = re.findall(r"\d\d\d",s)
j = [int(o) for o in k]
ss = list()
for k in range(max(j)):
	if k not in j:
		ss.append(k)
print(ss)
