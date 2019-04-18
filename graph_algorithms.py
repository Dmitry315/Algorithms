infinity = float('inf')


def dijkstra(graph, start, end):
    dist = {}
    for i in graph.keys():
        dist[i] = infinity if i != start else 0
    current_node = start
    visited = []
    unvisited = graph[start]
    unvisited[start] = 0
    while unvisited:
        for n in graph[current_node].keys():
            if n not in visited:
                distance = dist[current_node] + graph[current_node][n]
                dist[n] = distance if distance < dist[n] else dist[n]
                unvisited[n] = dist[n]
        visited.append(current_node)
        del unvisited[current_node]
        if unvisited:
            current_node = min(unvisited.keys(), key=lambda key: unvisited[key])
    return dist[end]


'''
graph = {
    'a': {'b': 1, 'c': 3, 'd': 4},
    'b': {'d': 2, 'e': 4},
    'c': {'d': 2, 'f': 3},
    'd': {'f': 5, 'e': 4},
    'f': {'g': 2},
    'e': {'g': 3},
    'g': {}
}
print(dijkstra(graph, 'a', 'g'))
'''