import networkx as nx
import matplotlib.pyplot as plt
import re

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_input(input_data):
    """
    Parse the input file generated to extract vertices, edges, and agent info.
    """
    vertices = []
    edges = []
    agents = {}

    # Creating regex expression objects for vertices, agents, and start/goal
    vertex_pattern = re.compile(r"vertex\(\((\d+),(\d+)\)\)\.")
    agent_pattern = re.compile(r"agent\((\d+)\)\.")
    start_pattern = re.compile(r"start\((\d+),\((\d+),(\d+)\)\)\.")
    goal_pattern = re.compile(r"goal\((\d+),\((\d+),(\d+)\)\)\.")

    # Parse vertices
    for match in vertex_pattern.finditer(input_data):
        x, y = map(int, match.groups())
        vertices.append((x, y))

    # Parse agents, starts, and goals
    for match in agent_pattern.finditer(input_data):
        agent_id = int(match.group(1))
        agents[agent_id] = {'start': None, 'goal': None}

    for match in start_pattern.finditer(input_data):
        agent_id, x, y = map(int, match.groups())
        agents[agent_id]['start'] = (x, y)

    for match in goal_pattern.finditer(input_data):
        agent_id, x, y = map(int, match.groups())
        agents[agent_id]['goal'] = (x, y)

    # Generate edges based on |X-X'| + |Y-Y'| = 1
    for (x, y) in vertices:
        for (x_prime, y_prime) in vertices:
            if abs(x - x_prime) + abs(y - y_prime) == 1:  # Manhattan distance = 1
                edges.append(((x, y), (x_prime, y_prime)))

    return vertices, edges, agents

def build_graph(vertices, edges, agents):
    """
    Build a NetworkX graph using the parsed data.
    """
    G = nx.Graph()
    G.add_nodes_from(vertices)
    G.add_edges_from(edges)

    #Add agent information as node attributes
    for agent_id, data in agents.items():
        if data['start'] in G.nodes:
            G.nodes[data['start']]['agent_start'] = agent_id
        if data['goal'] in G.nodes:
            G.nodes[data['goal']]['agent_goal'] = agent_id

    return G

def shortest_path(agents):
    short_path =[]
    for agent_id, agent_data in agents.items():
      start_node = agent_data['start']
      goal_node  = agent_data['goal']
      try:
        shortest_path = nx.shortest_path(G, start_node, goal_node)
        path_length = len(shortest_path) - 1
        short_path.append((agent_id,path_length))
      except nx.NetworkXNoPath:
        pass
    return short_path

def degree(agent):
  deg_start=[]
  deg_goal=[]
  deg=dict(G.degree)
  for agent_id, agent_data in agents.items():
    start_node = agent_data['start']
    goal_node  = agent_data['goal']
    deg_start.append((agent_id,deg[start_node]))
    deg_goal.append((agent_id,deg[goal_node]))
  return deg_start,deg_goal

def centrality(agent):
    bw=dict(nx.betweenness_centrality(G))
    start_centrality_bw = []
    goal_centrality_bw = []
    start_centrality_cl = []
    goal_centrality_cl = []
    for agent_id, agent_data in agents.items():
      start_node = agent_data['start']
      goal_node  = agent_data['goal']
      try:
        start_centrality_bw.append((agent_id,bw[start_node]))
        goal_centrality_bw.append((agent_id,bw[goal_node]))
        start_centrality_cl.append((agent_id,nx.closeness_centrality(G,start_node)))
        goal_centrality_cl.append((agent_id,nx.closeness_centrality(G,goal_node)))
      except nx.NetworkXError:
        pass
    return start_centrality_bw,goal_centrality_bw,start_centrality_cl,goal_centrality_cl

input_data = read_from_file("test-instance.lp")


# Automate the process
vertices, edges, agents = parse_input(input_data)
G = build_graph(vertices, edges, agents)
short_path = shortest_path(agents)
deg_start,deg_goal = degree(agents)
start_centrality_bw,goal_centrality_bw,start_centrality_cl,goal_centrality_cl = centrality(agents)

# Print and visualize the graph
print(short_path)



print("Results:")
print("-" * 30)
print("Shortest Path Length for each agent:")
for agent_id, path_length in short_path:
    print(f"  Agent {agent_id}: {path_length}")

print("\nDegree of Nodes:")
print("-" * 30)
print("  Start Nodes:")
for agent_id, degree in deg_start:
    print(f"    Agent {agent_id}: {degree}")
print()    
print("  Goal Nodes:")
for agent_id, degree in deg_goal:
    print(f"    Agent {agent_id}: {degree}")

print("\nCentrality Measures:")
print("-" * 30)
print("  Betweenness Centrality:")
print("    Start Nodes:")
for agent_id, centrality in start_centrality_bw:
    print(f"      Agent {agent_id}: {centrality}")
print("    Goal Nodes:")
for agent_id, centrality in goal_centrality_bw:
    print(f"      Agent {agent_id}: {centrality}")
print() 
print("  Closeness Centrality:")
print("    Start Nodes:")
for agent_id, centrality in start_centrality_cl:
    print(f"      Agent {agent_id}: {centrality}")
print("    Goal Nodes:")
for agent_id, centrality in goal_centrality_cl:
    print(f"      Agent {agent_id}: {centrality}")

    node_colors = ['lightblue' for _ in G.nodes]
for _,data in agents.items():
      node_colors[list(G.nodes).index(data['start'])] = 'green'  # Highlight start nodes in red
      node_colors[list(G.nodes).index(data['goal'])] = 'red'  # Highlight goal nodes in green

pos = {node: node for node in G.nodes()}  # Use node coordinates as positions
nx.draw_networkx(G, pos, with_labels=True, node_color=node_colors, font_weight='bold')
plt.show()

#PS C:\Users\Keerthan Shetty\OneDrive - KNIME AG\Desktop\Python\ASP\MAPF_with_Priority> py shortest_path.py