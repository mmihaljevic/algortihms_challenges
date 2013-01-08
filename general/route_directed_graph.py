"""
Given a directed graph, design an algorithm to find out whether there is a route be-
tween two nodes.

graph is represented by adjacency list
"""

def find_path(graph, node1, node2):
    # check if nodes are part of a graph
    # think is it better to return False or raise an exception?
    if not graph.has_key(node1) or not graph.has_key(node2):
        return False
    
    visited = []
    unvisited = [node1]
    while len(unvisited) > 0:
        node = unvisited.pop()
        children = graph[node]

        # maybe node doesn't have children
        if len(children) > 0:
            if node2 in children:
                return True
            visited.append(node)
            for child in children:
                # avoid cycles
                if child not in visited and child not in unvisited:    
                    unvisited.append(child)

    return False


# test graph
graph = { '1' : ['2'], '2' : ['5', '3'], '3': ['4'], '4': ['2', '5'],
          '5': ['6'] , '6': [], '8':['9', '10'], '10': [], '9':[]}

print find_path(graph, '1', '4')
print find_path(graph, '1', 10)
print find_path(graph, '4', '1')

    


