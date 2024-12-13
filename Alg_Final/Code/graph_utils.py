class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        if not any(neighbor == v for neighbor, _ in self.graph[u]):
            self.graph[u].append((v, weight))
            self.graph[v].append((u, weight))

    def get_nodes(self):
        return self.graph.keys()

    def get_edges(self):
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                if (v, u, weight) not in edges:
                    edges.append((u, v, weight))
        return edges

    def print_graph(self):
        print("\nGraph Representation:")
        for node, edges in self.graph.items():
            edge_descriptions = [f"({neighbor}, weight: {weight})" for neighbor, weight in edges]
            print(f"  {node}: {'; '.join(edge_descriptions)}")

    def is_connected(self):
        if not self.graph:
            return False
        visited = set()
        start_node = next(iter(self.graph))
        self._dfs_for_connectivity(start_node, visited)
        return len(visited) == len(self.graph)

    def _dfs_for_connectivity(self, node, visited):
        visited.add(node)
        for neighbor, _ in self.graph[node]:
            if neighbor not in visited:
                self._dfs_for_connectivity(neighbor, visited)

    @staticmethod
    def from_file(file_path):
        graph = Graph()
        with open(file_path, 'r') as file:
            for line in file:
                u, v, weight = line.strip().split()
                graph.add_edge(u, v, int(weight))
        return graph