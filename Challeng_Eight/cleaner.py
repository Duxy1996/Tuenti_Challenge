#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import unicodedata
import codecs
return_value = []
lines = codecs.open("testInput.txt","r",encoding="utf-16").readlines()

for line in lines:
	char = line.split("\\")
	char = unicodedata.normalize('NFKD', char[0]).encode('ascii','ignore')
	char = char.strip()
	#print(char)
	if char == "":
		return_value.append("N/A")
	else:
		return_value.append(char)
	#line_a = line.decode('utf-16').encode('utf-8')
	#text_file.write(line_a)

index = 0;
text_file = open("Output.txt", "w")
return_value.pop(0)
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	