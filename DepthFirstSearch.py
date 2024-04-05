def depthFirstSearch(graph, source, visited=None, path=None):
    if visited is None: #if No place is visited
        visited = set() #first create a set for visited places
    if path is None: #if there is no path which lead to destination, create a list for one
        path = []

    visited.add(source) #add visted nodes to the set
    path.append(source) #append the path which lead to desinttion

    if source == 'Gawadar': #if among the visited set of place, any node is ==Gawadar
        print("Successfully Arrived at Gawadar")
        print("Path: ", "->".join(path))
        return

    for neighbor in graph[source]: # for places in graph, startin from source
        if neighbor not in visited: #if any is not visited, call back dFS
            depthFirstSearch(graph, neighbor, visited, path[:])  # Pass a copy of the path

    if 'Gawadar' not in visited:
        print("Destination Not Found")

# Example Graph
graph = {
    'Peshawar': ['Islamabad', 'DIKhan'],
    'Islamabad': ['Peshawar','Lahore', 'Faisalabad'],
    'DIKhan': ['Peshawar','Faisalabad', 'Quetta'],
    'Faisalabad': ['DIKhan','Islamabad','Lahore', 'Multan'],
    'Lahore': ['Islamabad','Faisalabad','Multan'],
    'Multan': ['Faisalabad','Lahore','Shukkar'],
    'Quetta': ['DIKhan','Shukkar','Gawadar'],
    'Shukkar': ['Multan','Karachi', 'Quetta'],
    'Karachi': ['Shukkar','Gawadar'],
    'Gawadar':['Quetta','Karachi']
}

depthFirstSearch(graph, 'Peshawar')
