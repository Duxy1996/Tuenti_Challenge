days_file = open("submitInput.txt",'r')
return_value = []
tiradas = []
partidas = []
text = days_file.read();
text = text.split("\n")
text.pop(0)
for val in text:
	
	aux_val = val.split()
	aux_array = map(int,aux_val)
	if len(aux_array) > 1:	
		index = 0
		tirada_aux = [];		
		for spin in aux_array:
			if (index == 0) & (spin == 10):
				tirada_aux.append(spin)
				tiradas.append(tirada_aux)
				tirada_aux = []
			else:
				if index == 1:
					tirada_aux.append(spin)
					tiradas.append(tirada_aux)
					tirada_aux = []
					index = 0
				else:
					index = index + 1
					tirada_aux.append(spin)
		if index == 1:
			tiradas.append(tirada_aux)

		if len(tiradas) > 10:
			for value_aux_in in tiradas[len(tiradas)-1]:
				tiradas[len(tiradas)-2].append(value_aux_in)
			tiradas.pop()		
		partidas.append(tiradas)
		tiradas = []

for partida in partidas:
	#print (partida)
	sum_total = 0;
	puntos = []
	indice_tirada = 0
	for tirada in partida:
		indice_tirada = indice_tirada + 1
		if indice_tirada == 11:
			break
			sum_total = sum_total + sum(tirada)
		else:
			if (sum(tirada) == 10) & ( indice_tirada < len(partida)):
				if len(tirada) == 1:
					if len(partida[indice_tirada]) > 1:
						sum_total = sum_total + sum(tirada) + partida[indice_tirada][0]+partida[indice_tirada][1]
					else:
						sum_total = sum_total + sum(tirada) + partida[indice_tirada][0]+partida[indice_tirada+1][0]
				else:
					sum_total = sum_total + sum(tirada) + partida[indice_tirada][0]
			else:
				sum_total = sum_total + sum(tirada)
		puntos.append(sum_total)
	
	return_value.append(map(int,puntos))

index = 0;
text_file = open("Output.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+' '.join(map(str, val))+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()