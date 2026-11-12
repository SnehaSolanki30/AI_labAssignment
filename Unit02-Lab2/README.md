# Lab 2: Uninformed and Heuristic Search Algorithms

## 1. Aim / Problem Statement
To implement and compare uninformed and informed (heuristic) search algorithms for route planning and graph traversal[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span):
1. Breadth-First Search (BFS)[span_5](start_span)[span_5](end_span)
2. Depth-First Search (DFS)[span_6](start_span)[span_6](end_span)
3. Hill Climbing Search[span_7](start_span)[span_7](end_span)
4. Best-First Search[span_8](start_span)[span_8](end_span)
5. $A^{*}$ Search[span_9](start_span)[span_9](end_span)

## 2. Algorithm
* **BFS:** Explores nodes level by level using a FIFO queue; guarantees the shortest path in terms of edge count.
* **DFS:** Explores as deep as possible along each branch using a LIFO stack before backtracking.
* **Hill Climbing:** Local search algorithm that iteratively moves to the neighboring node with the lowest heuristic value $h(n)$.
* **Best-First Search:** Uses a priority queue to always expand the node closest to the goal based solely on heuristic $h(n)$.
* **$A^{*}$ Search:** Uses evaluation function $f(n) = g(n) + h(n)$ (actual path cost + heuristic estimate) to find the optimal lowest-cost path.

## 3. Results / Output
For path finding from Start Node **`A`** to Goal Node **`G`**:
* **BFS:** Path `['A', 'B', 'D', 'G']` | Cost: `8`
* **DFS:** Path `['A', 'B', 'D', 'G']` | Cost: `8`
* **Hill Climbing:** Path `['A', 'B', 'E', 'G']` | Cost: `7`
* **Best-First Search:** Path `['A', 'B', 'E', 'G']` | Cost: `7`
* **$A^{*}$ Search:** Path `['A', 'B', 'E', 'G']` | Cost: `7` (Optimal Path)

## 4. Performance Analysis
| Algorithm | Type | Complete? | Optimal? | Time Complexity | Execution Time |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BFS | Uninformed | Yes | Yes (unweighted) | $O(b^d)$ | ~0.02 ms |
| DFS | Uninformed | No | No | $O(b^m)$ | ~0.01 ms |
| Hill Climbing | Local Search | No | No | $O(\infty)$ | ~0.01 ms |
| Best-First Search | Informed | No | No | $O(b^m)$ | ~0.02 ms |
| $A^{*}$ Search | Informed | Yes | Yes | $O(b^d)$ | ~0.02 ms |

## 5. Learning Outcomes
* Understood the difference between **Uninformed Search** (BFS, DFS) and **Informed/Heuristic Search** (Best-First, $A^{*}$)[span_10](start_span)[span_10](end_span).
* Analyzed how $A^{*}$ guarantees an optimal solution using $f(n) = g(n) + h(n)$, whereas Hill Climbing can get stuck in local optima[span_11](start_span)[span_11](end_span).
*
