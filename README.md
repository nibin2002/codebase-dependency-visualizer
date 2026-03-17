# Codebase Dependency Visualizer

##  Overview

A Python tool that analyzes a codebase and visualizes dependencies between 
modules. It parses import statements and generates an interactive network 
graph showing relationships between files.

##  Features

* Scans Python files in a directory
* Extracts import dependencies
* Generates interactive graph visualization (HTML)
* Ranks files based on number of dependencies

## ️ Technologies Used

* Python
* PyVis (interactive graphs)
* NetworkX (graph structure)

## ️ How to Run

```bash
pip3 install pyvis networkx
python3 main.py
```

Enter the folder path when prompted.

##  Output

* Terminal: Dependency map + ranking
* Browser: Interactive graph (`dependency_graph.html`)

##  Sample Output

(See screenshot below)

## Use Case

Helps developers understand project structure and identify highly 
dependent modules.

##  Future Enhancements

* Highlight critical modules
* Add filtering options
* Convert into web application

