#!/usr/bin/env python3
#
# Dallas Foglia
# 2017/9/3
#
# Editor" tabstops = 2, cols = 80
#
# Depth First Search for dfs numbered nodes.
# Tested on Fig 6.38, page 226 of Data Structures and Algorithms text.
#
# Written for Python3

#search directed graph input
def search(dGraph):
	nodes = []
	while len(dGraph) > len(nodes):
		for element in dGraph:
			if element not in nodes:
				nodes.append(element)
				print(nodes)
				for edge in dGraph[element]:
					if edge not in nodes:
						nodes.append(edge)
						print(nodes)
	return nodes

#dictionary keys act as 'nodes', key values are their connected node.
example = {'a':['b','d','f'],
				'b':['c','f'],
				'c':['d'],
				'd':['b'],
				'e':['d','f'],
				'f':['d']}

#so I'm not quite sure what's going on here. it performs the search
#correctly, but it seems to pick a node at random to perform the operation
#to perfrom the search on. or I might be wring and it's working incorrectly.
#(0_0)
nodes = search(example)
print(nodes)
