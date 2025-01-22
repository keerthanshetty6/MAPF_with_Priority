def dfs(graph, u, visited, stack):
    """Visit function for Depth First Search (DFS)."""
    # Mark the node as visited
    visited.add(u)

    # For every course (v) that depends on course u (outgoing edge)
    for v in graph.get(u, []):
        if v not in visited:  # If v is not visited
            dfs(graph, v, visited, stack)  # Recursively visit v

    # After all neighbors are visited, add the node to the stack
    stack.append(u)

def depth_first_search(graph):
    """Perform DFS on the graph starting from nodes with no incoming edges."""
    # Initialize visited set to avoid revisiting nodes
    visited = set()
    
    # Stack to store topological order
    stack = []

    # Find nodes with no prerequisites (no incoming edges)
    start_nodes = []
    for course, prerequisites in graph.items():
        if len(prerequisites) == 0:  # No prerequisites for this course
            start_nodes.append(course)

    # Reverse the graph: prerequisite -> courses (adjacency list)
    adj_graph = {}
    for course, prerequisites in graph.items():
        for prerequisite in prerequisites:
            if prerequisite not in adj_graph:
                adj_graph[prerequisite] = []
            adj_graph[prerequisite].append(course)

    # Start the DFS by visiting the start_nodes
    for node in start_nodes:
        if node not in visited:
            dfs(adj_graph, node, visited, stack)
    
    # Return the topological order (reversed stack)
    return stack[::-1]  # Reverse the stack to get the correct order

# Sample course data (course -> prerequisites)
courses = {
    "Math": [],
    "Physics": ["Math"],
    "Chemistry": ["Math"],
    "Biology": ["Chemistry"],
    "Computer Science": ["Math", "Physics"],
    "Algorithms": ["Computer Science"],
    "Data Structures": ["Computer Science"],
    "Machine Learning": ["Algorithms", "Data Structures"],
    "AI": ["Machine Learning"],
    "Databases": ["Data Structures"]
}

# Run DFS and topological sort
topological_order = depth_first_search(courses)

# Print the topological order
print("Topological Order:", topological_order)
