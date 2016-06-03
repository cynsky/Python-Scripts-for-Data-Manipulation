import re 
lines = [line.strip() for line in open('H:\data viz personal\DATA\states.csv')]
for x in lines:
	match = re.sub("[\(\[].*?[\)\]]", "", x)
	if match: print match
