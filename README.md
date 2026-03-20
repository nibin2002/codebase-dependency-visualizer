# Codebase Dependency Visualizer

A professional Python tool that analyzes a codebase and visualizes module dependencies using both interactive and high‑resolution static graphs.

Designed to help developers understand project structure, identify tightly coupled modules, and analyze dependency flow efficiently.

---

## Overview

This tool scans a Python codebase, extracts import relationships, and generates visual and analytical outputs that make dependency structures easy to understand.

---

## Features

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

```bash
python3 main.py
```

When prompted, enter the folder path of the Python project you want to analyze:

```
Enter folder path: /path/to/your/project
```

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

![Dependency Graph](dependency_graph.png)

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

