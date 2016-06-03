#looks for state abbreviations in brackets
import re
lines = [line.strip() for line in open('Data\states.csv')]
for x in lines:
	match = re.findall(r"\[(.*)\]", x)
	if match: print match
