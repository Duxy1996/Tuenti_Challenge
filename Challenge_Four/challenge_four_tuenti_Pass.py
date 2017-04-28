days_file = open("submitInput.txt",'r')
#days_file = open("testInput.txt",'r')
text = days_file.read();
text = text.split("\n")
text.pop(0)
text.pop()
return_value = []
print (len(text))
for triangulos in text:
	triangulos_sp = triangulos.split()
	triangulos_sp = map(int,triangulos_sp)
	triangulos_sp.pop(0)
	triangulos_sp.sort()
	index_tri = 0
	res = 0
	index_of_range = 0
	menor = 9999999999999999999999999999

	for lado in range(0,len(triangulos_sp)):
		for lado2 in range(lado+1,len(triangulos_sp)):
			for lado3 in range(lado2+1,len(triangulos_sp)):
				a = triangulos_sp[lado]
				b = triangulos_sp[lado2]
				c = triangulos_sp[lado3]
				if (a+b >c)&(a+c>b)&(c+b>a)&(a+b+c<menor):
					menor = a+b+c
					#print(a,b,c)					
					break				
				#print(a,b,c)
	if menor == 9999999999999999999999999999:
		return_value.append("IMPOSSIBLE")	
	else:
		return_value.append(menor)	
	

index = 0;
text_file = open("OutputBreak.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	