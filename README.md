# Codebase Dependency Visualizer

A professional Python tool that analyzes a codebase and visualizes module dependencies using both interactive and high‑resolution static graphs.

Designed to help developers understand project structure, identify tightly coupled modules, and analyze dependency flow efficiently.

---

## Overview

This tool scans a Python codebase, extracts import relationships, and generates visual and analytical outputs that make dependency structures easy to understand.

---

## Features

### Architecture Overview

The tool follows a simple pipeline:

1. **File Discovery** — Recursively locates Python source files
2. **Import Extraction** — Parses dependency statements using regex
3. **Graph Construction** — Builds a directed dependency graph
4. **Metric Computation** — Calculates in-degree and out-degree
5. **Visualization** — Generates interactive and static graphs

### Codebase Analysis

* Recursively scans all Python files in a directory
* Parses `import` and `from ... import ...` statements
* Builds a dependency map between modules automatically

### Dependency Metrics

* **Out-degree** — Number of modules a file imports
* **In-degree** — Number of modules that import a file
* Clear terminal summaries for quick inspection
* Automatic ranking by most dependent modules

### Interactive Visualization

* Dynamic dependency network rendered in browser
* Drag, zoom, and explore module relationships
* Physics-based layout for clean structure
* Suitable for live exploration and demos

### Static Graph Export

* High‑resolution PNG export
* Professional dark theme
* Node sizes proportional to dependency count
* Directional edges with arrows
* Suitable for reports and documentation

---

## Technology Stack

* Python — Core language
* PyVis — Interactive network visualization
* NetworkX — Graph construction and metrics
* Matplotlib — Static graph rendering

---

## Installation

```bash
pip3 install pyvis networkx matplotlib
```

---

## Usage

### Basic Run

```bash
python3 main.py
```

When prompted, enter the folder path of the Python project you want to analyze:

```
Enter folder path: /path/to/your/project
```

### Example

```bash
python3 main.py
Enter folder path: ./my_project
```

The tool will analyze the codebase and generate both visual and analytical outputs automatically.

---

## Outputs

### Terminal

* Dependency map
* In-degree and Out-degree summary
* Ranking by outgoing dependencies

### Interactive Graph

```
dependency_graph.html
```

Open in a browser to explore the network dynamically.

### Static Graph Image

```
dependency_graph.png
```

High‑resolution dependency graph with proportional node sizing.

---

## Example Insights

* Identify highly dependent modules
* Detect architectural bottlenecks
* Spot reusable utility modules
* Understand overall project structure quickly

---

## Sample Output

### Static Dependency Graph

High-resolution export generated using NetworkX and Matplotlib.

![Dependency Graph](dependency_graph.png)

### Interactive Dependency Graph

Browser-based interactive visualization generated using PyVis.

* Zoom and pan navigation
* Draggable nodes
* Physics-based layout
* Clear directional relationships

File: `dependency_graph.html`

---

## Use Cases

* Codebase onboarding
* Architecture reviews
* Refactoring planning
* Academic projects
* Technical documentation

---

## Future Enhancements

* Centrality analysis for critical module detection
* Community detection for module clustering
* Import type classification (standard library vs third‑party vs local)
* Command-line argument support
* Web dashboard interface

---

## Author

Nibin Varughese Alex
M.Tech Computer Science
Focus areas: Developer tools, visualization, applied software engineering

---

## License

MIT License

