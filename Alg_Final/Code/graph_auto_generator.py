import random
from graph_utils import Graph

def auto_generate_graphs(num_graphs, min_nodes=5, max_nodes=20, min_edges=5, max_edges=50, max_weight=10):
    """
    Automatically generate a list of graphs with varying nodes, connections, and edge weights.

    Args:
        num_graphs (int): Number of graphs to generate.
        min_nodes (int): Minimum number of nodes in a graph.
        max_nodes (int): Maximum number of nodes in a graph.
        min_edges (int): Minimum number of edges in a graph.
        max_edges (int): Maximum number of edges in a graph.
        max_weight (int): Maximum weight for an edge.

    Returns:
        list: A list of generated Graph objects.
    """
    graphs = []

    for _ in range(num_graphs):
        # Randomize the number of nodes and edges for each graph
        num_nodes = random.randint(min_nodes, max_nodes)
        max_possible_edges = num_nodes * (num_nodes - 1) // 2  # Max edges in a fully connected graph
        num_edges = min(random.randint(min_edges, max_edges), max_possible_edges)

        # Create a graph
        graph = Graph()

        # Generate unique node labels
        nodes = [f"Node_{i}" for i in range(num_nodes)]

        # Add edges
        edges = set()
        edge_count = 0
        while edge_count < num_edges:
            # Randomly pick two distinct nodes
            u, v = random.sample(nodes, 2)

            # Avoid duplicate edges (u, v) or (v, u)
            if (u, v) not in edges and (v, u) not in edges:
                weight = random.randint(1, max_weight)
                graph.add_edge(u, v, weight)
                edges.add((u, v))
                edge_count += 1

        graphs.append(graph)

    return graphs
