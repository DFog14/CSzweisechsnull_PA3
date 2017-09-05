#!/usr/bin/env python3
#
# Dallas Foglia
# 2017/9/4
#
# Editor: tabstops = 2, cols = 80
#
# Dijkstra's Alogrithm with adjaceny matrix representaion of graph.
#
# Written for Python 3

INF = 99999

#[x,y], where x represents the a list and y represensts and element.
matrix =[[INF, 4, 1, 5, 8, 10],
			[INF, INF, INF, INF, INF, INF],
			[INF, 2, INF, INF, INF, INF],
			[INF, INF, INF, INF, 2, INF],
			[INF, INF, INF, INF, INF, 1],
			[INF, INF, INF, INF, INF, INF]]


