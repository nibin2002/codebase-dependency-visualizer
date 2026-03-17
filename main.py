import os
import re
from pyvis.network import Network

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
# PRINT OUTPUT
# =========================
print("\nDependency Map:")
for file, deps in dependency_map.items():
    print(f"{file} → {deps}")

print("\nRanking (Most Dependencies First):")
sorted_files = sorted(dependency_map.items(), key=lambda x: len(x[1]), reverse=True)

for file, deps in sorted_files:
    print(f"{file}: {len(deps)} dependencies")


# =========================
# INTERACTIVE GRAPH
# =========================
net = Network(height="750px", width="100%", bgcolor="#0d1117", font_color="white")

# Add nodes
for file in dependency_map:
    net.add_node(file, label=file, color="#1f77b4", size=25)

# Add external nodes + edges
for file, deps in dependency_map.items():
    for dep in deps:
        if dep not in dependency_map:
            net.add_node(dep, label=dep, color="#2ecc71", size=20)
        net.add_edge(file, dep)

# Physics settings (smooth movement)
net.barnes_hut(
    gravity=-3000,
    central_gravity=0.3,
    spring_length=150,
    spring_strength=0.05,
    damping=0.09
)

# Save and open in browser
net.write_html("dependency_graph.html")
