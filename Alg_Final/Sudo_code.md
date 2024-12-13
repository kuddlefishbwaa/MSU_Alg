# Pseudocode for All Components

## **Graph Class**

### `add_edge(u, v, weight)`
```plaintext
IF u is not in graph:
    Initialize graph[u] as an empty list
IF v is not in graph:
    Initialize graph[v] as an empty list
IF edge (u, v) does not already exist:
    Add (v, weight) to graph[u]
    Add (u, weight) to graph[v]
```

### `get_nodes()`
```plaintext
RETURN all keys in graph
```

### `get_edges()`
```plaintext
Initialize edges as an empty list
FOR each node u in graph:
    FOR each (neighbor, weight) in graph[u]:
        IF (neighbor, u, weight) is not in edges:
            Add (u, neighbor, weight) to edges
RETURN edges
```

### `print_graph()`
```plaintext
FOR each node in graph:
    Print node and its list of neighbors with weights
```

### `is_connected()`
```plaintext
IF graph is empty:
    RETURN False
Initialize visited as an empty set
Start DFS from an arbitrary node in graph
RETURN True if all nodes are visited; otherwise, False
```

## **Algorithms Module**

### `dijkstra(graph, start)`
```plaintext
Initialize distances for all nodes as infinity
Set distances[start] = 0
Initialize priority queue with (0, start)

WHILE priority queue is not empty:
    Pop the node with the smallest distance
    FOR each neighbor of the current node:
        Calculate new distance via the current node
        IF new distance < current distance for the neighbor:
            Update distances[neighbor]
            Push (new distance, neighbor) to the priority queue

RETURN distances
```

### `a_star(graph, start, goal, heuristic)`
```plaintext
Initialize distances for all nodes as infinity
Set distances[start] = 0
Initialize priority queue with (0, start)

WHILE priority queue is not empty:
    Pop the node with the lowest cost
    IF current node == goal:
        RETURN distances[goal]
    FOR each neighbor of the current node:
        Calculate new cost via the current node
        IF new cost < current distance for the neighbor:
            Update distances[neighbor]
            Push (new cost + heuristic(neighbor, goal), neighbor) to the priority queue

RETURN infinity if goal is not reachable
```

### `kruskal(graph)`
```plaintext
Sort all edges by weight
Initialize each node as its own parent
Initialize MST as empty and total_weight = 0

FOR each edge (u, v, weight) in sorted edges:
    IF u and v are in different sets:
        Add edge to MST
        Merge the sets of u and v
        Add weight to total_weight

RETURN MST and total_weight
```

### `dfs(graph, start)`
```plaintext
Initialize visited as an empty set
Initialize stack with start node
Initialize traversal as an empty list

WHILE stack is not empty:
    Pop a node from the stack
    IF node is not visited:
        Mark node as visited
        Add node to traversal
        Add all unvisited neighbors of the node to the stack

RETURN traversal
```

### `bfs(graph, start)`
```plaintext
Initialize visited as an empty set
Initialize queue with start node
Initialize traversal as an empty list

WHILE queue is not empty:
    Dequeue a node from the queue
    IF node is not visited:
        Mark node as visited
        Add node to traversal
        Add all unvisited neighbors of the node to the queue

RETURN traversal
```

## **AutoGraphGen Module**

### `auto_generate_graphs(num_graphs, min_nodes, max_nodes, min_edges, max_edges, max_weight)`
```plaintext
Initialize graphs as an empty list

FOR i in range(num_graphs):
    Randomly determine number of nodes and edges
    Initialize an empty graph
    Generate unique node labels
    Add random edges with weights while ensuring no duplicates
    Add the generated graph to the list of graphs

RETURN graphs
```

## **MLRecommender Module**

### `extract_features(graph)`
```plaintext
Compute number of nodes
Compute number of edges
Compute density = num_edges / (num_nodes * (num_nodes - 1))
Compute average edge weight
Check if graph is connected
RETURN these features as a list
```

### `simulate_data(graphs, heuristic)`
```plaintext
Initialize feature matrix X and labels y

FOR each graph in graphs:
    Extract features
    Select two nodes for start and goal
    Apply all algorithms and record execution times
    Identify the best algorithm (minimum time)
    Append features and best algorithm to X and y

RETURN X and y
```

### `train_model(X, y)`
```plaintext
Split X and y into training and testing sets
Train a DecisionTreeClassifier on the training set
Evaluate model on the testing set
RETURN the trained model
```

### `recommend_algorithm(graph, model)`
```plaintext
Extract features from the input graph
Predict the best algorithm using the trained model
RETURN the name of the recommended algorithm
```

## **Main Module**

### `load_test_graph()`
```plaintext
Prompt user to load a graph from a file or input manually
IF file:
    Read and parse the file to create a graph
ELSE:
    Manually create a graph by adding nodes and edges
RETURN the created graph
```

### `heuristic(node, goal)`
```plaintext
RETURN a constant heuristic value (e.g., 1)
```

### `main()`
```plaintext
Generate random graphs for training
Simulate data and train the model
Load a test graph
Recommend the best algorithm for the test graph
```
