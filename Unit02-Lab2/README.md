# Lab 2: Uninformed & Informed (Heuristic) Search Algorithms

## 1. Aim / Problem Statement
To implement and compare uninformed and heuristic-driven graph search algorithms across 5 standalone Python programs:
1. **Breadth-First Search (`1_BreadthFirstSearch.py`):** Explore a graph level-by-level using a FIFO Queue to find the shortest path in terms of edges.
2. **Depth-First Search (`2_DepthFirstSearch.py`):** Explore graph branches deeply using Recursion/Stack traversal.
3. **Hill Climbing Search (`3_HillClimbing.py`):** Perform local greedy heuristic optimization by always moving toward a lower heuristic state.
4. **Greedy Best-First Search (`4_BestFirstSearch.py`):** Use a Priority Queue ordered strictly by heuristic estimate $h(n)$ to reach the goal quickly.
5. **A* (A-Star) Optimal Search (`5_AStarSearch.py`):** Find the optimal lowest-cost path using $f(n) = g(n) + h(n)$.

## 2. How to Run
```bash
python 1_BreadthFirstSearch.py
python 2_DepthFirstSearch.py
python 3_HillClimbing.py
python 4_BestFirstSearch.py
python 5_AStarSearch.py
