#Dijkstra's Algorithm
import pandas as pandas
import numpy as np
from sys import argv
from collections import defaultdict, deque


#read in the graph
#edge 1 : {nodes}, {length}
def read_graph(filename):
	graph = {}
	nodes = set()
	with open(filename,"r") as text:
		for line in text:
			print("LINE")
			key = int(line.split('\t')[0])
			print(key)
			edges = map(lambda s: s.strip(),  line.split('\t')[1:])
			print(edges)
			edges = [e.split(",") for e in edges]
			graph[key] = {}
			for i in range(0,len(edges)-1):
				graph[key][int(edges[i][0])] = {}
				graph[key][int(edges[i][0])] = int(edges[i][1])
	return graph



#Mark all nodes unvisited. 
#Create a set of the unvisited nodes called the 
#unvisited set consisting of all the nodes.
#wikipedia algorithm & stack overflow help
def dijikstras_algorithm(graph, start):
	nodes = graph.keys()
	not_visited = {node: None for node in nodes}
	#visited will keep track of the times
	visited = {}
	#starting point
	current = start
	current_distance = 0
	not_visited[current] = current_distance

	while True:
		#iterate over each child of current node
		for node, distance in graph[current].items():	
			if node not in not_visited: continue
			#compute it's tentative distances
			new_distance = distance + current_distance
			if not_visited[node] == None or not_visited[node] > new_distance:
				not_visited[node] = new_distance
			#once we iterated through all the children then we will have the
			#smallest distances per node in not_visited
		#mark current node as visited
		visited[current] = current_distance
		del not_visited[current]
		if not not_visited: break
		#reset current and distance to the smallest distance
		#if node is in visited and is not none
		next_node = [node for node in not_visited.items() if node[1]]
		#sort on the value (k, v) x[1] and provide the first element from list
		current, current_distance = sorted(next_node, key = lambda x: x[1])[0]
	return visited


if __name__ == "__main__":
	#Read in graph
	filename = argv[1]
	graph = read_graph(filename)
	#Do the algorithm
	output = dijikstras_algorithm(graph, 1)
	#spit out homework answers
	homework_list = [7,37,59,82,99,115,133,165,188,197]
	for i in homework_list:
		print("{} has {}".format(i, output[i]))

