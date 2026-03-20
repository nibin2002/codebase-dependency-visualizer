import os
import re
from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt

# =========================
# GET PY FILES
# =========================
def get_python_files(folder):
    python_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


# =========================
# EXTRACT IMPORTS
# =========================
def extract_imports(file_path):
    imports = []
    try:
        with open(file_path, "r") as file:
            content = file.read()
            imports += re.findall(r'import (\w+)', content)
            imports += re.findall(r'from (\w+) import', content)
    except:
        pass
    return imports


# =========================
# MAIN
# =========================
folder_path = input("Enter folder path: ")

files = get_python_files(folder_path)
dependency_map = {}

for file in files:
    filename = os.path.basename(file)
    imports = extract_imports(file)
    dependency_map[filename] = imports


# =========================
# BUILD NETWORKX GRAPH
# =========================
G = nx.DiGraph()

for file in dependency_map:
    G.add_node(file)

for file, deps in dependency_map.items():
    for dep in deps:
        G.add_node(dep)
        G.add_edge(file, dep)

# Degrees
in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())


# =========================
# PRINT OUTPUT
# =========================
print("\nDependency Map:")
for file, deps in dependency_map.items():
    print(f"{file} → {deps}")

print("\nFile Degree Summary:")
for node in G.nodes():
    print(f"{node} → In-degree: {in_degrees.get(node,0)}, Out-degree: {out_degrees.get(node,0)}")

print("\nRanking (Most Outgoing Dependencies First):")
sorted_files = sorted(out_degrees.items(), key=lambda x: x[1], reverse=True)

for file, degree in sorted_files:
    print(f"{file}: {degree} outgoing dependencies")


# =========================
# STATIC GRAPH EXPORT
# =========================
plt.figure(figsize=(12, 8))

node_sizes = [800 + (out_degrees.get(node, 0) ** 1.8) * 900 for node in G.nodes()]
pos = nx.spring_layout(G, k=0.8)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=node_sizes,
    node_color="#4F46E5",
    edge_color="#9CA3AF",
    font_color="white",
    font_size=10,
    width=1.2,
    arrows=True,
    arrowsize=12
)

ax = plt.gca()
ax.set_facecolor('#0f172a')
plt.title("Code Dependency Graph", color="white", fontsize=16, pad=20)

plt.savefig(
    "dependency_graph.png",
    dpi=300,
    facecolor='#0f172a',
    bbox_inches='tight'
)
plt.close()

print("\nSaved static graph as dependency_graph.png")


# =========================
# INTERACTIVE GRAPH (BIGGER CIRCLE)
# =========================
net = Network(height="900px", width="100%", bgcolor="#0d1117", font_color="white")

# Better layout
net.force_atlas_2based()

# Nodes
for file in dependency_map:
    net.add_node(file, label=file, color="#1f77b4", size=25)

# Edges
for file, deps in dependency_map.items():
    for dep in deps:
        if dep not in dependency_map:
            net.add_node(dep, label=dep, color="#2ecc71", size=20)
        net.add_edge(file, dep)

# Spacious circular physics
net.barnes_hut(
    gravity=-8000,
    central_gravity=0.6,
    spring_length=300,
    spring_strength=0.03,
    damping=0.12
)

net.write_html("dependency_graph.html")
print("Saved interactive graph as dependency_graph.html")
