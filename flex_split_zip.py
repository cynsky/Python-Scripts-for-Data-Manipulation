import re
lines = [line.split('-')[0] for line in open('H:\data viz personal\DATA\zip.csv')]
for x in lines:
	match = re.findall(r"(?:-)(.*)", x)
	if match:
		print match
	else: 
		print x
