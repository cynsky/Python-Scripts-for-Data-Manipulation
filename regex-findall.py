
import re
lines = [line.strip() for line in open('H:\data viz personal\DATA\states.csv')]
for x in lines:
	match = re.findall(r"\((.*)\)", x)
	if match: print match
