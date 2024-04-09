import heapq

def aStarSearch(graph, start, goal):
    priority_queue = [(0, start)]  # Priority queue of tuples (f_cost, node)
    visited = set()
    parent = {}

    while priority_queue:
        f_cost, node = heapq.heappop(priority_queue)  # Dequeue node with lowest f_cost
        if node == goal:
            return reconstruct_path(parent, start, goal)  # Return the path to reach the goal
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    g_cost = f_cost - heuristic(node, goal)  # Correcting the calculation of g_cost
                    h_cost = heuristic(neighbor, goal)
                    f_cost = g_cost + h_cost
                    heapq.heappush(priority_queue, (f_cost, neighbor))
                    parent[neighbor] = node

    return []  # Return an empty path if no path found

def heuristic(node, goal):
    # Heuristic function: Euclidean distance between two cities
    city_coordinates = {
        'Peshawar': (0, 0),
        'Islamabad': (100, 200),
        'DIKhan': (150, 50),
        'Faisalabad': (300, 100),
        'Lahore': (400, 200),
        'Multan': (500, 0),
        'Quetta': (400, -200),
        'Shukkar': (600, 100),
        'Karachi': (700, 0),
        'Gawadar': (800, -200)
    }
    x1, y1 = city_coordinates[node]
    x2, y2 = city_coordinates[goal]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def reconstruct_path(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    return path[::-1]

# Example Graph with weighted edges
graph = {
    'Peshawar': [('Islamabad', 1), ('DIKhan', 4)],
    'Islamabad': [('Peshawar', 1), ('Lahore', 3), ('Faisalabad', 4)],
    'DIKhan': [('Peshawar', 4), ('Faisalabad', 3), ('Quetta', 5)],
    'Faisalabad': [('DIKhan', 3), ('Islamabad', 4), ('Lahore', 1), ('Multan', 2)],
    'Lahore': [('Islamabad', 3), ('Faisalabad', 1), ('Multan', 3)],
    'Multan': [('Faisalabad', 2), ('Lahore', 3), ('Shukkar', 4)],
    'Quetta': [('DIKhan', 5), ('Shukkar', 5), ('Gawadar', 6)],
    'Shukkar': [('Multan', 4), ('Karachi', 5), ('Quetta', 5)],
    'Karachi': [('Shukkar', 5), ('Gawadar', 5)],
    'Gawadar': [('Quetta', 6), ('Karachi', 5)]
}

# Example usage
source_node = 'Peshawar'
destination_node = 'Gawadar'
path = aStarSearch(graph, source_node, destination_node)
if path:
    print("Path from", source_node, "to", destination_node, ":", "->".join(path))
else:
    print("No path found from", source_node, "to", destination_node)
