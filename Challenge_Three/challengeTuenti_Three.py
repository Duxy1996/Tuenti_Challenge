days_file = open("submitInput.txt",'r')
#days_file = open("testInput.txt",'r')
text = days_file.read();
text = text.split("\n")
#print text
text.pop(0)
text.pop()
#print text
return_value = []
for elemnts in text:	
	aux_el = elemnts
	iterations_until_end = 0
	while aux_el > 1:
		iterations_until_end = iterations_until_end +1
		aux_el = int(round(int(aux_el)/2.0))
		#print aux_el
	return_value.append(iterations_until_end)
	#print iterations_until_end
index = 0;
text_file = open("Output2.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	