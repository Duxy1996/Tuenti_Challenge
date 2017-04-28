days_file = open("submitInput.txt",'r')
#days_file = open("testInput.txt",'r')
text = days_file.read();
text = text.split("\n")
text.pop(0)
text.pop()
return_value = []
print (len(text))
index_time = len(text)
for triangulos in text:
	triangulos_sp = triangulos.split()
	triangulos_sp = map(int,triangulos_sp)
	triangulos_sp.pop(0)
	triangulos_sp.sort()
	index_tri = 0
	res = 0
	index_of_range = 0
	menor = Integer.MAX_VALUE

	for lado in range(0,len(triangulos_sp)):
		a = triangulos_sp[lado]
		if (a > menor):
			break
		for lado2 in range(lado+1,len(triangulos_sp)):
			b = triangulos_sp[lado2]
			if (a+b > menor):
				break
			for lado3 in range(lado2+1,len(triangulos_sp)):	
				c = triangulos_sp[lado3]
				if (a+b >c)&(a+c>b)&(c+b>a)&(a+b+c<menor):
					menor = a+b+c
					#print(a,b,c)					
					break				
				#print(a,b,c)
	if menor == Integer.MAX_VALUE:
		return_value.append("IMPOSSIBLE")	
	else:
		return_value.append(menor)	
	print(index_time)
	index_time = index_time -1

index = 0;
text_file = open("Outputfast.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	