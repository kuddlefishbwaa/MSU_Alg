import heapq

# Algorithms

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    total_weight = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.graph[current_node]:
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                total_weight += weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))

    return {node: dist for node, dist in distances.items() if dist < float('infinity')}, total_weight

def a_star(graph, start, goal, heuristic):
    distances = {node: float('infinity') for node in graph.graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    total_weight = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            return distances[goal], total_weight

        for neighbor, weight in graph.graph[current_node]:
            new_cost = distances[current_node] + weight

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                total_weight += weight
                heapq.heappush(priority_queue, (new_cost + heuristic(neighbor, goal), neighbor))

    return distances.get(goal, float('infinity')), total_weight

def kruskal(graph):
    edges = graph.get_edges()
    edges.sort(key=lambda x: x[2])

    parent = {}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    mst = []
    total_weight = 0

    for node in graph.get_nodes():
        parent[node] = node

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            stack.extend(neighbor for neighbor, _ in graph.graph[node] if neighbor not in visited)

    return traversal

def bfs(graph, start):
    visited = set()
    queue = [start]
    traversal = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(neighbor for neighbor, _ in graph.graph[node] if neighbor not in visited)

    return traversal

def topological_sort(graph):
    in_degree = {node: 0 for node in graph.get_nodes()}
    for node in graph.get_nodes():
        for neighbor, _ in graph.graph[node]:
            in_degree[neighbor] += 1

    zero_in_degree = [node for node, degree in in_degree.items() if degree == 0]
    topo_order = []

    while zero_in_degree:
        node = zero_in_degree.pop(0)
        topo_order.append(node)
        for neighbor, _ in graph.graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(topo_order) == len(graph.get_nodes()):
        return topo_order
    else:
        raise ValueError("The graph is not a Directed Acyclic Graph (DAG).")