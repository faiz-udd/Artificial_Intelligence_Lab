from collections import deque

def breadthFirstSearch(graph, source):
    visited = set()
    queue = deque([source])  # Initialize the queue with the source node
    parent = {source: None}  # Keep track of parent nodes for constructing the path

    while queue:
        current_node = queue.popleft()  # Dequeue the front node from the queue
        visited.add(current_node)  # Mark the current node as visited

        # Check if the destination is reached
        if current_node == 'Gawadar':
            print("Successfully Arrived at Gawadar")
            print("Path:", reconstruct_path(parent, source, current_node))
            return

        # Enqueue all unvisited neighbors of the current node
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = current_node  # Record the parent of each neighbor

    print("Destination Not Found")

def reconstruct_path(parent, source, destination):
    # Reconstruct the path from the destination to the source
    path = [destination]
    while path[-1] != source:
        path.append(parent[path[-1]])
    path.reverse()
    return '->'.join(path)

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

breadthFirstSearch(graph, 'Peshawar')
