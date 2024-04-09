import math
from queue import PriorityQueue

# Heuristic function (distance to goal)
def heuristic(node, goal):
    # Assuming node and goal are city names
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
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Greedy Best-First Search function
def greedyBFS(graph, start, goal):
    queue = PriorityQueue()  # Priority Queue based on Heuristic Value
    queue.put((0, start))
    visited = set()
    parent = {}  # Dictionary to store parent nodes

    while not queue.empty():
        _, current_node = queue.get()

        if current_node == goal:
            return reconstruct_path(parent, start, goal)  # Reconstruct path if goal is found

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                priority = heuristic(neighbor, goal)  # Compute Heuristic Value
                queue.put((priority, neighbor))
                parent[neighbor] = current_node  # Store parent node for reconstruction

    return []  # Return an empty path if goal is not found

# Function to reconstruct the path from parent pointers
def reconstruct_path(parent, start, goal):
    path = [goal]
    while path[-1] != start:
        if path[-1] not in parent:  # If no path exists
            return "No path found"
        path.append(parent[path[-1]])
    return path[::-1]  # Reverse the path to get the correct order

# Example Graph
graph = {
    'Peshawar': ['Islamabad', 'DIKhan'],
    'Islamabad': ['Peshawar', 'Lahore', 'Faisalabad'],
    'DIKhan': ['Peshawar', 'Faisalabad', 'Quetta'],
    'Faisalabad': ['DIKhan', 'Islamabad', 'Lahore', 'Multan'],
    'Lahore': ['Islamabad', 'Faisalabad', 'Multan'],
    'Multan': ['Faisalabad', 'Lahore', 'Shukkar'],
    'Quetta': ['DIKhan', 'Shukkar', 'Gawadar'],
    'Shukkar': ['Multan', 'Karachi', 'Quetta'],
    'Karachi': ['Shukkar', 'Gawadar'],
    'Gawadar': ['Quetta', 'Karachi']
}

# Example usage
source_node = 'Peshawar'
destination_node = 'Gawadar'
result = greedyBFS(graph, source_node, destination_node)
print(result)
