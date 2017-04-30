import codecs

days_file = open("testInput.txt",'r',encoding='utf-8')
print days_file
text = days_file.read();

text = text.split("\n")
text.pop(0)
text.pop()
return_value = []

for num in text:
	print num

index = 0;
text_file = open("Output.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	