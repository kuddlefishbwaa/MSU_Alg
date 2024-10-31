import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import random

def create_hyper_ring_graph(n, max_edges=None):
    """Create a Hyper Ring Graph with n nodes and limit on edges per node."""
    G = nx.Graph()
    
    if max_edges is None:
        max_edges = n.bit_length()  # Default to the current maximum number of edges based on powers of 2

    for u in range(n):
        edges_added = 0  # Counter for edges added
        for power in range(n.bit_length()):  # Check powers of 2
            if edges_added < max_edges:  # Only add edges up to the limit
                v = (u + (1 << power)) % n
                if not G.has_edge(u, v):  # Avoid adding the same edge twice
                    G.add_edge(u, v)
                    edges_added += 1

    return G

def create_connectivity_matrix(G):
    """Create and return the connectivity matrix as a Pandas DataFrame."""
    adjacency_matrix = nx.to_numpy_array(G)
    df = pd.DataFrame(adjacency_matrix, columns=range(len(G.nodes)), index=range(len(G.nodes)))
    return df

def perform_dfs_from_matrix(matrix):
    """Perform DFS using the connectivity matrix and return the traversal order."""
    start_node = 0  # Start from the first node
    visited = set()  # Keep track of visited nodes
    traversal_order = []  # Store the order of traversal

    def dfs(node):
        visited.add(node)  # Mark the current node as visited
        traversal_order.append(node)  # Add it to the traversal order
        # Iterate through all possible neighbors
        for neighbor in range(len(matrix)):
            # Check if there is an edge and if the neighbor has not been visited
            if matrix[node][neighbor] == 1 and neighbor not in visited:
                dfs(neighbor)  # Recursively call DFS on the neighbor

    dfs(start_node)  # Start DFS from the initial node
    return traversal_order

def perform_bfs_from_matrix(matrix):
    """Perform BFS using the connectivity matrix and return the traversal order."""
    start_node = 0  # Start from the first node
    visited = set()  # Keep track of visited nodes
    traversal_order = []  # Store the order of traversal
    queue = [start_node]  # Initialize the queue with the starting node

    while queue:
        node = queue.pop(0)  # Dequeue the first node
        if node not in visited:  # Only process if it hasn't been visited
            visited.add(node)  # Mark the current node as visited
            traversal_order.append(node)  # Add it to the traversal order
            # Iterate through all possible neighbors
            for neighbor in range(len(matrix)):
                # Check if there is an edge and if the neighbor has not been visited
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    queue.append(neighbor)  # Enqueue the neighbor for later processing

    return traversal_order

def animate_search(matrix, traversal_order, algorithm):
    """Animate the search through the graph."""
    pos = nx.circular_layout(G)  # Position nodes in a circular layout

    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Initial graph display
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)

    # Animation function
    def update(num):
        ax.clear()  # Clear the current axes
        # Draw the entire graph
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=10)
        
        # Highlight the current node
        current_node = traversal_order[num]
        nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='orange', node_size=700)

        # Highlight the edge leading to the current node from the previous node
        if num > 0:  # Skip for the first node
            previous_node = traversal_order[num - 1]
            if matrix[previous_node][current_node] == 1:  # Check if there is an edge
                nx.draw_networkx_edges(G, pos, edgelist=[(previous_node, current_node)], edge_color='orange', width=4)

        ax.set_title(f"{algorithm} Traversal: {current_node}")

    ani = animation.FuncAnimation(fig, update, frames=len(traversal_order), repeat=False, interval=1)  # Slowed down
    plt.show()

def main():
    try:
        n = int(input("Enter the number of nodes: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Get the maximum number of edges per node
        max_edges_input = input("Enter the maximum number of edges per node (or press Enter for default): ")
        max_edges = int(max_edges_input) if max_edges_input else None

        # Create the Hyper Ring Graph with edge limitation
        global G  # Make G global to use in animation
        G = create_hyper_ring_graph(n, max_edges)

        # Create and display the connectivity matrix
        connectivity_matrix = create_connectivity_matrix(G)
        print("\nConnectivity Matrix:")
        print(connectivity_matrix)

        # Convert the DataFrame to a NumPy array for easy access
        matrix_array = connectivity_matrix.values

        # Choose algorithm
        algorithm = input("Choose an algorithm (DFS/BFS): ").strip().upper()
        if algorithm == 'DFS':
            traversal_order = perform_dfs_from_matrix(matrix_array)
            print(f"DFS Traversal Order: {traversal_order}")
            animate_search(matrix_array, traversal_order, "DFS")
        elif algorithm == 'BFS':
            traversal_order = perform_bfs_from_matrix(matrix_array)
            print(f"BFS Traversal Order: {traversal_order}")
            animate_search(matrix_array, traversal_order, "BFS")
        else:
            print("Invalid algorithm selected. Please choose 'DFS' or 'BFS'.")

    except ValueError:
        print("Invalid input. Please enter an integer for the number of nodes and edges.")

if __name__ == "__main__":
    main()
