#!/usr/bin/env python3
#
# Dallas Foglia
# 2017/9/4
#
# Editor: tabstops = 2, cols = 80
#
# Dijkstra's shortest path algorithm using a partially ordered tree
# as a prioirity queue and link adjacency lists as the graph.
#
# Written for Python3

import PointerList as PL

#Starting from the bottom. coordinate, cost, coordinate, cost, ....
x = PL.PointerList()
x.insert(1,x.first())
x.insert([1,2],x.first())
x.insert(1,x.first())
x.insert([1,3],x.first())
x.insert(5,x.first())
x.insert([1,4],x.first())
x.insert(8,x.first())
x.insert([1,5],x.first())
x.insert(10,x.first())
x.insert([1,6],x.first())
x.insert(2,x.first())
x.insert([3,2],x.first())
x.insert(2,x.first())
x.insert([4,5],x.first())
x.insert(1,x.first())
x.insert([5,6],x.first())

#Returns distances between x = 1 through y = 1 thorugh 6
def nodeDistances(tree):
	temp = []
	for i in range(0,5):
		temp.append(tree[(tree.index([1,i+2])-1)])
	return temp

def dijkstra(tree, distances):
	temp = []
	for i in range(0,5):
		small_node = tree[tree.index(min(distances)+1)]
		temp.append(small_node)
		small_dist = min(distances)
		del distances[min(distances)]
		for item in distances:
			if [small_dist, item] in distances:
				if item > (small_dist + tree[(tree.index([small_dist, item])-1)]):
					item = small_dist + tree[(tree.index([small_dist, item])-1)]
			print("Dist: {}".format(distances))
			print("Temp: {}".format(temp))

#Distance, [Coordinate], .....
#Coordinate index minus one gives associated distance index
y = [1,[5,6],2,[4,5],2,[3,2],10,[1,6],8,[1,5],5,[1,4],1,[1,3],1,[1,2]]
dists = nodeDistances(y)
dijkstra(y, dists)
