import os
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("./"):
    f.extend(filenames)
    break

def banana():
	out = ""
	for i in range(0, len(f)):
		if f[i] == "test.py":
			f[i] = f[i].replace("test.py", '')
		out += '"%s", ' % (f[i]).replace(".png", "")
	return out



print(banana())