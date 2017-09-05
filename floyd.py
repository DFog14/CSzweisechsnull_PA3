#!/usr/bin/env python3
#
# Dallas Foglia
# 2017/9/3
#
# Editor tabstops = 2, cols = 80
#
# Floyd's Algorithm. Recovering paths
# Test on prob. 6 in review 2, which in no longer on the website. Y?
# 
# A[1,2]=4 A[1,3]=1 A[1,4]=5 A[1,5]=8 A[1,6]=10 A[3,2]=2 A[4,5]=2 A[5,6]=1 
#
# Written for Python3

#Large Value that represents no path.
MAX_INT = 99999
N_SIZE =  6 #Array Size

def floyd(grid):
	temp = {0: grid}
	for k in range(1, N_SIZE+1):
		temp[k] = {}
		for i in range(1, N_SIZE+1):
			for j in range(1, N_SIZE+1):
				temp[k][i,j] = min(temp[k-1][i,j], temp[k-1][i,k] + temp[k-1][k,j])
	return temp[N_SIZE]

#grid is represented by dict using tuples as positions
def initGrid():
	grid = {}
	for i in range(1,N_SIZE+1):
		grid[i,i] = 0
		for j in range(1,N_SIZE+1):
			grid.setdefault((i,j), MAX_INT)

	return grid

#Add values to grid
G = initGrid()
G[1,2] = 4
G[1,3] = 1
G[1,4] = 5
G[1,5] = 8
G[1,6] = 10
G[3,2] = 2
G[4,5] = 2
G[5,6] = 1
floydG = floyd(G)

#Print list by list
for i in range(1, 6):
	l = []
	for j in range(1,6):
		l.append(floydG[i,j])
	print(l)
