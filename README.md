# Best First Search Algorithm in Python

This project demonstrates the implementation of the Best First Search algorithm using Python. The algorithm explores a graph by selecting the node with the lowest heuristic value at each step, making it an informed search strategy.

## Overview

Best First Search is a graph traversal technique that uses a heuristic function to decide which node to visit next. It prioritizes nodes that appear to be closer to the goal based on the given heuristic values.

## Features

* Uses a priority queue to always expand the most promising node
* Supports any graph represented as an adjacency list
* Allows custom heuristic values for each node
* Stops execution when the goal node is reached

## Algorithm Steps

1. Initialize a priority queue and insert the start node with its heuristic value
2. Repeat until the queue is empty:

   * Remove the node with the smallest heuristic value
   * If it has not been visited, mark it as visited
   * If it is the goal node, terminate the search
   * Otherwise, add all unvisited neighbors to the queue with their heuristic values

## Input

* Graph represented as a dictionary of adjacency lists
* Start node
* Goal node
* Heuristic values for each node

## Output

* Prints the order of visited nodes
* Displays a message when the goal node is reached

## Example

Graph:
S → A, B
A → C, D
B → E

Heuristic Values:
S = 5
A = 3
B = 4
C = 2
D = 6
E = 1

Start Node: S
Goal Node: E

## How to Run

1. Ensure Python is installed on your system
2. Copy the code into a Python file, for example best_first_search.py
3. Run the script using:

python best_first_search.py

## Applications

* Pathfinding problems
* Artificial Intelligence search tasks
* Game development
* Navigation systems

## License

This project is open-source and available for educational purposes.


