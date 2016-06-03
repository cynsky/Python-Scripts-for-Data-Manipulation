#prints 5-digit zip code only and deletes second half
import re
lines = [line.split('-')[0] for line in open('Data\zip.csv')]
for x in lines:
	match = re.findall(r"(?:-)(.*)", x)
	if match:
		print match
	else: 
		print x
