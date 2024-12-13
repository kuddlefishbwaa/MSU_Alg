from graph_auto_generator import auto_generate_graphs
from ml_recommender import simulate_data, train_model, recommend_algorithm
from graph_utils import Graph
import random

def load_test_graph():
    """
    Allow the user to load a test graph from a file or manually input graph details.

    Returns:
        Graph: The loaded or manually created graph.
    """
    print("Do you want to load a graph from a file? (y/n)")
    choice = input().strip().lower()

    if choice == 'y':
        try:
            print("Enter the file path:")
            file_path = input().strip()
            graph = Graph.from_file(file_path)
            print("Graph successfully loaded from file.")
        except Exception as e:
            print(f"Failed to load graph from file: {e}")
            graph = None
    else:
        print("Enter details to manually create a graph.")
        graph = Graph()
        try:
            print("Enter the number of nodes (default is a random value between 5 and 15):")
            num_nodes_input = input().strip()
            num_nodes = int(num_nodes_input) if num_nodes_input else random.randint(5, 15)

            print("Enter the number of edges (default is a random value between 10 and 20):")
            num_edges_input = input().strip()
            num_edges = int(num_edges_input) if num_edges_input else random.randint(10, 20)

            print("Now, enter each edge in the format 'node1 node2 weight' (or press Enter to auto-generate all edges):")
            edges_entered = False

            for _ in range(num_edges):
                edge_input = input("Edge: ").strip()
                if edge_input:
                    edges_entered = True
                    edge_parts = edge_input.split()
                    if len(edge_parts) != 3:
                        print("Invalid edge format. Please enter in the format 'node1 node2 weight'.")
                        continue

                    node1, node2, weight = edge_parts
                    weight = int(weight)
                    graph.add_edge(node1, node2, weight)

            if not edges_entered:
                print("Auto-generating edges...")
                for _ in range(num_edges):
                    node1 = f"Node_{random.randint(0, num_nodes - 1)}"
                    node2 = f"Node_{random.randint(0, num_nodes - 1)}"
                    while node1 == node2:
                        node2 = f"Node_{random.randint(0, num_nodes - 1)}"
                    weight = random.randint(1, 10)
                    graph.add_edge(node1, node2, weight)

            print("Graph successfully created.")
        except Exception as e:
            print(f"Error creating graph: {e}")
            graph = None

    return graph

def heuristic(node, goal):
    """
    Placeholder heuristic function for A*.

    Args:
        node: The current node.
        goal: The goal node.

    Returns:
        int: A constant heuristic value.
    """
    return 1

def main():
    # Generate random graphs for simulation
    print("Generating random graphs...")
    num_graphs = 10
    generated_graphs = auto_generate_graphs(
        num_graphs=num_graphs,
        min_nodes=5,
        max_nodes=15,
        min_edges=10,
        max_edges=20,
        max_weight=10
    )

    # Simulate data for training
    print("Simulating data...")
    X, y = simulate_data(generated_graphs, heuristic)

    # Check if there is sufficient data
    if len(X) == 0 or len(y) == 0:
        print("Insufficient data to train the model.")
        return

    # Train the model
    print("Training the model...")
    model = train_model(X, y)

    # Load test graph
    print("\nLoading the test graph...")
    test_graph = load_test_graph()

    if test_graph:
        test_graph.print_graph()
        # Recommend the best algorithm
        print("\nRecommending the best algorithm for the test graph...")
        recommend_algorithm(test_graph, model)

if __name__ == "__main__":
    main()
