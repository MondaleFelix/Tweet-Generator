import re

text = open("corpus.txt", "r+")

lines = text.readlines()

for line in lines: 
	line = line.replace("“", " ")
	line = line.replace("”", " ")
	line = line.replace("_", "")
	line = line.replace("-", "")


 lines = " ".join(lines)
