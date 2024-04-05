import heapq
def uniformCostSearch(graph, source, destination):
    priority_queue = [(0, source)]  # Priority queue of tuples (cost, node)
    visited = set()
    parent ={}

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)  # Dequeue node with lowest cost
        if node == destination:
            return cost, path_followed(parent, source, destination)  # Return the cost to reach the destination
        if node not in visited:
            visited.add(node)
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + neighbor_cost, neighbor))
                    parent[neighbor]=node

    return float('inf')  # Return infinity if destination is not reachable

#path Followed Function
def path_followed(parent, source, destination):
    path =[]
    current_node = destination
    while current_node!=source:
        path.append(current_node)
        current_node= parent[current_node]
    path.append(source)
    path.reverse()
    return path

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
cost, path= uniformCostSearch(graph, source_node, destination_node)
if cost != float('inf'):
    print(f"Minimum cost to reach {destination_node} from {source_node}:", cost, " Kilometers")
    print("Path:","->".join(path))
else:
    print(f"No path found from {source_node} to {destination_node}")
