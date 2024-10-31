import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

def generate_maze(rows, cols):
    # Create a graph
    G = nx.grid_2d_graph(rows, cols)

    # Create a list to store the edges in the maze
    maze_edges = []
    traversal_path = []

    # Use DFS to create the maze
    stack = []
    visited = set()
    
    # Start from a random cell
    start = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    stack.append(start)
    visited.add(start)

    while stack:
        current = stack[-1]
        traversal_path.append(current)
        neighbors = []

        # Check each possible direction (up, down, left, right)
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and
                    neighbor not in visited):
                neighbors.append(neighbor)

        if neighbors:
            # Choose a random unvisited neighbor
            next_cell = random.choice(neighbors)
            # Add the edge to the maze
            maze_edges.append((current, next_cell))
            stack.append(next_cell)
            visited.add(next_cell)
        else:
            stack.pop()

    return G, maze_edges, traversal_path

def update(frame):
    plt.clf()  # Clear the current figure
    plt.title("Maze Generation Animation")
    
    # Draw the maze edges
    maze_graph = nx.Graph()
    for edge in maze_edges[:frame + 1]:
        maze_graph.add_edge(edge[0], edge[1])
    
    pos = {(x, y): (y, -x) for x, y in G.nodes()}
    
    # Draw the maze
    nx.draw(maze_graph, pos, with_labels=False, node_size=50, edge_color='black')

    # Highlight walls that were not removed
    for edge in G.edges():
        if edge not in maze_edges:
            plt.plot([pos[edge[0]][0], pos[edge[1]][0]], 
                     [pos[edge[0]][1], pos[edge[1]][1]], 
                     color='gray', linewidth=0.5, alpha=0.3)

    # Highlight the traversal path
    if frame < len(traversal_path) - 1:
        plt.plot([pos[traversal_path[frame]][0], pos[traversal_path[frame + 1]][0]], 
                 [pos[traversal_path[frame]][1], pos[traversal_path[frame + 1]][1]], 
                 color='Green', linewidth=5)

    plt.axis('off')

# Define maze dimensions
rows, cols = 25, 25

# Generate the maze
G, maze_edges, traversal_path = generate_maze(rows, cols)

# Set up the figure for animation
fig = plt.figure(figsize=(10, 10))
num_frames = len(maze_edges)  # Total frames based on the number of edges added

# Create an animation
ani = FuncAnimation(fig, update, frames=num_frames, repeat=False)

plt.show()

