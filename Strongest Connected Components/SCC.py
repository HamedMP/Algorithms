#Computing Strong Components
#This algorithm is used to find all the Strong Connected COmponents.
#We run DFS twice first on the reversed directed graph
#and then another time substituing the nodes names for thier finishing times
#then at the end 


#to determin if opbject is in list use set
#to iterate use lists
#When implementing DFS iteratively, you should use collections.deque for the stack, which is optimized for quickly appending and popping elements.

import pandas as pandas
import numpy as np
from sys import argv
from collections import defaultdict, deque

#Read in graph
filename = argv[1]
graph_txt = open(filename)

def read_graph(filename, reverse):
	graph = defaultdict(list)
	with open(filename,"r") as text:
	    for line in text:
	    	if reverse:
	    		value, key = line.strip().split()
	    	else:
	        	key, value = line.strip().split()
	        graph[key].append(value)
	return(graph)

def highest_number_node(dictionary):
	'''what if the highest node is not a node that points anywhere?
		find highest number node'''
	v = [int(item) for sublist in list(dictionary.values()) for item in sublist]
	k = [int(item) for item in list(dictionary.keys())]
	if max(k) > max(v):
		return(max(k))
	else:
		return(max(v))

#won't do recursively since others have discussed issues doing
#that in python
def dfs_finishing_time(graph, start):
	'''depth first search and to output the finishing times
	Help from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
	'''
	#--set up visited and stack
	assert type(start) == str, "Input start to dfs_finishing time needs to be a string"
	visited = set()
	finishing_nodes = {}
	time = 1
	#--Start at the remaining highest node and go through it's path
	for start_dfs_node in range(int(start), 0, -1):
		#--Check if it was already visited in a path before
		start_dfs_node = str(start_dfs_node)
		if start_dfs_node not in visited:
			#stack = [str(start_dfs_node)]
			stack = deque([str(start_dfs_node)])
			while stack:
				vertex = stack.pop()
				#is the vertex not visited?
				if vertex not in visited:
					#--Add the vertex to visited
					visited.add(vertex)
					#exploring.append(vertex)
					stack.append(vertex)
					#--Add on the vertex's children to the stack
					stack.extend(set(graph[str(vertex)]) - visited)
					#--Mark it's finishing time if no children left
					if not set(graph[str(vertex)]) - visited:
						finishing_nodes[vertex]= time
						time = time + 1
				else:
					#--if the vertex is explored and all children
					#explored and not in nodes
					if vertex not in set(finishing_nodes):
						#print("Finishing {}".format(vertex))
						finishing_nodes[vertex]= time
						time = time + 1
	#print("Visited: {}".format(visited))
	#print("Exploring {}".format(exploring))
	#print("Finishing Times {}".format(nodes))
	return finishing_nodes


def dfs_leaders(graph, start, mapping):
	'''depth first search and to output the leaders and their sizes
	'''
	#--set up visited and stack
	visited = set()
	leaders = []
	size_of_scc = []
	time = 1
	#--Start at the remaining highest node and go through it's path
	for start_dfs_node in range(int(start), 0, -1):
		size = 0
		#--Check if it was already visited in a path before
		if start_dfs_node not in visited:
			leaders.append(start_dfs_node)
			stack = [start_dfs_node]
			while stack:
				#print("Visited: {}".format(visited))
				vertex = stack.pop()
				#print("Vertex is {}".format(vertex))
				if vertex not in visited:
					size = size + 1
					#print("Vertex {} not in visited".format(vertex))
					#--Add the vertex to visited
					visited.add(vertex)
					#--Add on the vertex's children to the stack
					stack.extend(set(graph[vertex]) - visited)	
			size_of_scc.append(size)
	return size_of_scc

#need to get the size
#normal graph
print("Reading in graph")
graph = read_graph(filename, False)
num_of_nodes = highest_number_node(graph)
print("We have {} number of nodes".format(num_of_nodes))

#insert reversed graph into this first pass
print("First DFS- getting finishing times")
finishing_time = dfs_finishing_time(read_graph(filename, reverse=True), str(num_of_nodes) )
print(finishing_time)

print("Begin Graph reassign")
#reassign the graph? or finda way to map it?
graph_reassign = defaultdict(list)
for k in graph:
	new_key = finishing_time[str(k)]
	for v in graph[k]:
		new_value = finishing_time[v]
		graph_reassign[new_key].append(new_value)
print("Graph reassign complete")
#del graph

#output size of strongest connected components
print("Last dfs")
size_of_scc = dfs_leaders(graph_reassign, num_of_nodes, finishing_time)
print(sorted(size_of_scc, reverse=True))






