#days_file = open("submitInput.txt",'r')
days_file = open("testInput.txt",'r')
text = days_file.read();
text = text.split("\n")
text.pop(0)
text.pop()
return_value = []
indexx = 0;
for case in text:
	indexx = indexx+1
	case_a = case.split()
	case_a = map(float,case_a)

	if case_a[1] % 2 != 0:
		case_a[1]=case_a[1] - 1

	if case_a[1] < 4:
		return_value.append(0)
	else:
		value = 4
		if (case_a[1] % 4 == 0):
			if (case_a[0]+2*case_a[2]) % 2 != 0:
				case_a[0] = case_a[0] - 1	
			if(case_a[0] == 0):
				if(case_a[1] <= 4):
					case_a[2]= case_a[2]-1

			#value = (case_a[0])+(case_a[1])+(case_a[2])
			if (case_a[1] < 0):
				case_a[1] = 0
			if (case_a[0] < 0):
				case_a[0] = 0
			if (case_a[2] < 0):
				case_a[2] = 0
			if(case_a[2] == case_a[0] == 0)&(case_a[1] < 12):
				case_a[1] = 4

			return_value.append(int(case_a[1])+int(case_a[0])+int(case_a[2]))

		else:
			return_value.append(value)
index = 0;
text_file = open("Output.txt", "w")
for val in return_value:
	index = index + 1
	text_file.write("Case #"+str(index)+": "+str(val)+"\n")
	print ("Case #"+str(index)+": "+str(val))	
text_file.close()	