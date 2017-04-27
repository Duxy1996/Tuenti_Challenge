days_file = open("submitInput.txt",'r')
return_value = []
text = days_file.read();
text = text.split("\n")
text.pop(0)
for val in text:
	aux_val = val.split()
	aux_array = map(float,aux_val)
	if len(aux_array) > 1:
		return_value.append(sum(aux_array));
return_value = map(lambda x: x/8+0.49,return_value)
return_value = map(lambda x: round(x),return_value)
return_value =  map(int,return_value)
index = 0;
text_file = open("Output.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()