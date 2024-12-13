from graph_utils import Graph  # Import the Graph class
from Alg_Final.Code.algorithms import dijkstra, a_star, kruskal, dfs, bfs, topological_sort  # Import algorithms
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils.class_weight import compute_class_weight

def extract_features(graph):
    """
    Extract features from a graph for machine learning input.

    Args:
        graph (Graph): The graph object.

    Returns:
        list: A list of features including number of nodes, number of edges,
              density, average edge weight, and connectivity.
    """
    num_nodes = len(graph.get_nodes())
    num_edges = len(graph.get_edges())
    density = num_edges / (num_nodes * (num_nodes - 1)) if num_nodes > 1 else 0
    avg_weight = np.mean([weight for _, _, weight in graph.get_edges()]) if num_edges > 0 else 0
    is_connected = graph.is_connected()
    return [num_nodes, num_edges, density, avg_weight, int(is_connected)]

def simulate_data(graphs, heuristic):
    """
    Simulate a dataset from a list of graphs by applying algorithms and extracting features.

    Args:
        graphs (list): List of Graph objects.
        heuristic (function): Heuristic function for the A* algorithm.

    Returns:
        tuple: Features (X) and labels (y) for machine learning.
    """
    X = []
    y = []
    for graph in graphs:
        features = extract_features(graph)
        nodes = list(graph.get_nodes())

        if len(nodes) < 2:
            print(f"Skipping graph with {len(nodes)} node(s).")
            continue

        start_node = nodes[0]
        goal_node = nodes[1] if len(nodes) > 1 else start_node

        try:
            algorithm_times = [
                dijkstra(graph, start_node)[1],
                a_star(graph, start_node, goal_node, heuristic)[1],
                kruskal(graph)[1],
                len(dfs(graph, start_node)),
                len(bfs(graph, start_node))
            ]
            best_algorithm = np.argmin(algorithm_times)  # Index of the best algorithm
            X.append(features)
            y.append(best_algorithm)
        except Exception as e:
            print(f"Error processing graph: {e}")
            continue

    return np.array(X), np.array(y)

def train_model(X, y):
    """
    Train a decision tree classifier on the provided features (X) and labels (y).

    Args:
        X (numpy.ndarray): Feature matrix.
        y (numpy.ndarray): Labels array.

    Returns:
        model (DecisionTreeClassifier): The trained decision tree model.
    """
    # Check class balance and compute weights
    unique_classes = np.unique(y)  # Ensure unique_classes is a numpy array
    if len(unique_classes) > 1:
        class_weights = compute_class_weight(class_weight='balanced', classes=unique_classes, y=y)
        class_weights_dict = {cls: weight for cls, weight in zip(unique_classes, class_weights)}
    else:
        class_weights_dict = {unique_classes[0]: 1.0}  # If only one class exists, no balancing needed

    # Train-test split
    if len(X) < 2:
        print("Dataset too small for train-test split. Training on the entire dataset.")
        model = DecisionTreeClassifier(random_state=42, class_weight=class_weights_dict)
        model.fit(X, y)
        return model

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = DecisionTreeClassifier(random_state=42, class_weight=class_weights_dict)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    return model

def recommend_algorithm(graph, model):
    """
    Recommend the best algorithm for a given graph using the trained model.

    Args:
        graph (Graph): The graph object.
        model (DecisionTreeClassifier): The trained decision tree model.

    Returns:
        str: Recommended algorithm.
    """
    features = extract_features(graph)
    algorithms = ["Dijkstra", "A*", "Kruskal", "DFS", "BFS"]
    prediction = model.predict([features])[0]
    recommendation = algorithms[prediction]
    print(f"Recommended Algorithm: {recommendation}")
    return recommendation
