from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        #print(q)
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    return_value = []
    days_file = open("submitInput.txt",'r')
    text = days_file.read();
    text = text.split("\n")
    text.pop(0)
    text.pop()
    return_value = []
    cases = []
    index = -1
    for line in text:
        aux_arry = line.split()
        if len(aux_arry) == 2:
            index = index +1
            cases.append([line])
        else:
            cases[index].append(line)
    index = 0;
    text_file = open("OutputfastEntr4.txt", "w")
    edgi = 0
    for case in cases:
    	edgi = edgi +1
    	s = [0]
    	if edgi < 508:
	       	edges = []
	        #print case
	        first_ed = case.pop(0)
	        first_ed = first_ed.split()
	        first_ed.pop()
	        ed = int(first_ed[0])

	        #for first_ed in range(1,ed):
	            #edges.append((str(first_ed-1),str(first_ed),0))

	        for first_ed in range(0,ed): 
	            #print (first_ed,first_ed+1,first_ed)
	            edges.append((str(first_ed),str(first_ed+1),first_ed)) 

	        for shrc in case:            
	            shrc_a = shrc.split()
	            #print shrc_a
	            #modificar esto para que el atajo pueda ir desde cualquier camino hasta arriba
	            for edi in range(int(shrc_a[0]),int(shrc_a[1])):
	                #print(edi)
	                edges.append((str(edi),str(shrc_a[1]),int(shrc_a[2])))

	        #print "0 -> "+str(ed)
	        s = dijkstra(edges, "0", str(ed))	    
        #print ("resultado")
        index = index + 1
        print("Case #"+str(index)+": "+str(s[0]))
        text_file.write("Case #"+str(index)+": "+str(s[0])+"\n")        
        #return_value.append(s[0])
    text_file.close()    
    
    
    

    