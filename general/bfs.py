"""
Breadth first search implementation 
- input - graph represented in adjecency list
  {1:[2,3,4], 2:[1,6],...}
- O(V+E)
- vertices go from 1...n not 0..n-1
"""
from collections import deque

def bfs(graph, s):
	if graph is None or s is None:
		return False

	vertices = graph.keys()
	color = [0 for i in xrange(len(vertices) + 1)] # 0 - white, 1 - gray, 2 - black
	d = [65536 for i in xrange(len(vertices) + 1)] # distance to 'infinity'
	queue = deque([s])
	parent = [None for i in xrange(len(vertices) + 1)]
	color[s] = 1
	d[s] = 0
	while len(queue) > 0:
		u = queue.popleft()
		for v in graph[u]:
			if color[v] == 0:
				queue.append(v)
				d[v] = d[u] + 1
				parent[u] = v
				color[v] = 1
		color[u] = 2
	return d[1:]


adj_list = {1: [2,5], 2: [1, 5, 3, 4], 3: [2, 4], 4: [3, 2, 5], 5: [1, 2, 4]}
print bfs(adj_list, 3) 
