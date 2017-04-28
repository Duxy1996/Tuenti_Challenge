#days_file = open("submitInput.txt",'r')
days_file = open("testInput.txt",'r')
text = days_file.read();
text = text.split("\n")
text.pop(0)
text.pop()
return_value = []
for triangulos in text:
	triangulos_sp = triangulos.split()
	triangulos_sp = map(int,triangulos_sp)
	triangulos_sp.pop(0)
	triangulos_sp.sort()
	index_tri = 0
	res = 0
	for lado in triangulos_sp:
		if index_tri + 1 + 1 < len(triangulos_sp) :
			index_tri2 = index_tri + 1
			index_tri3 = index_tri2 + 1
			a = triangulos_sp[index_tri]			
			b = triangulos_sp[index_tri2]
			c = triangulos_sp[index_tri3]
			ant = a
			bnt = b
			cnt = c
			aux_index_tri = index_tri
			aux_index_tri2 = index_tri2
			aux_index_tri3 = index_tri3


			while((c+a>b)&(c+b>a)):
				if ((aux_index_tri3 == aux_index_tri) | (aux_index_tri2 == aux_index_tri3)):					
					break
				cnt = c
				c = triangulos_sp[aux_index_tri3]
				if (aux_index_tri3 == 0):
						break;	
				aux_index_tri3 = aux_index_tri3 -1
			c = cnt	

			while((a+b>c) & (b+c>a)):
				if ((aux_index_tri2 == aux_index_tri) | (aux_index_tri2 == aux_index_tri3)):					
					break
				bnt = b
				b = triangulos_sp[aux_index_tri2]
				if (aux_index_tri2 == 0):
						break;
				aux_index_tri2 = aux_index_tri2 -1
			b = bnt	

			while((a+b>c) & (a+c>b)):
				ant = a
				a = triangulos_sp[aux_index_tri]
				if (aux_index_tri == 0):
						break;
				aux_index_tri = aux_index_tri -1
			a = ant		

			if (a + b > c)&(b + c > a)&(a + c >b):
				res = 1;
				return_value.append(a+b+c)
				break
			index_tri = index_tri + 1
	if res == 0:
		return_value.append("IMPOSSIBLE")

index = 0;
text_file = open("Output.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	