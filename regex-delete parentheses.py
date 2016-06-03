#prints state name only in each row
import re 
lines = [line.strip() for line in open('Data\states.csv')]
for x in lines:
	match = re.sub("[\(\[].*?[\)\]]", "", x)
	if match: print match
