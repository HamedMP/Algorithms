import pandas as pd
import csv
import random
import sys

#randomize
random.seed(random.randint(0,10000000))
counts = []
iterations = int(float(sys.argv[1]))

for i in range(0,iterations): 
	print(i)
	#open file
	graph = []
	#with open("kargerMinCut.txt") as f:
	with open("small_graph.txt")
	    for line in f:
	    	line = line.strip()
	    	line = line.split(" ")
	    	#line = line.split("\t")
	    	graph.append(line)
	#print("Graph loaded")

	def pick_random_edge(graph):
		'''choose random edge'''
		random_line = random.choice(graph)
		edge_u = random_line[0]
		#pick random within that line
		edge_v = random.choice(random_line[1:len(random_line)])
		name = '{}_{}'.format(edge_u, edge_v)
		return edge_u, edge_v, name


	def karger_min_cut(graph):
		if len(graph) == 2:
			return graph, len(graph[0]) - 1
		#Pick a random edge
		edge_u, edge_v, name = pick_random_edge(graph)
		#Contraction
		hold = []
		#Remove edge_u line in the graph
		for i in graph:
			if i[0] == edge_u:
				graph.remove(i)
				hold = i #to append on to the edge_v graph
		#Update graph with new edge and remove self loops
		for j, i in enumerate(graph):
			if i[0] == edge_v:
				i[0]=name
				i.extend(hold)
				#remove all instances of edge_u and edge_v (self-loops)
				i = [x for x in i if x != edge_u]
				i = [x for x in i if x != edge_v]
				#i.insert(0, name)
			else:
				#Replace all instances of old node to new name
				if edge_u in i:
					i = map(lambda x:x if x!= edge_u  else name, i)
				if edge_v in i:		
					i = map(lambda x:x if x!= edge_v  else name, i)
			#replace line with new edits
			graph[j]= i
		return karger_min_cut(graph)

	graph, length = karger_min_cut(graph)
	counts.append(length)

print("Min value element : {} ".format(min(counts)))



#updates one day
#instead of looking through all the remaning lists in teh graph look at only the ones 
#that are specified in that node that was changed

