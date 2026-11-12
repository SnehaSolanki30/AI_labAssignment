# Lab 1: AI Problem Formulation & Production Systems

## 1. Aim / Problem Statement
To understand AI problem formulation, state-space representation, and implement rule-based production systems:
1. **Water Jug Problem:** Measure 2 liters of water using a 4-liter and a 3-liter jug.
2. **Vacuum Cleaner Agent:** Clean a two-location environment (`A` and `B`) using a simple reflex agent.
3. **Rule-Based Medical Diagnosis System:** Identify possible illnesses based on patient symptoms using `IF-THEN` production rules.

## 2. Algorithm
* **Water Jug Problem:** Uses Breadth-First Search (BFS) to explore valid state transitions (Fill, Empty, Pour) while keeping track of visited states to guarantee the shortest path.
* **Vacuum Cleaner Agent:** Uses a simple condition-action rule (`IF status == Dirty THEN Suck ELSE Move`) until all rooms are clean.
* **Medical Diagnosis System:** Matches patient symptom sets against predefined `IF-THEN` rules using subset matching.

## 3. Results / Output
* **Water Jug Problem:**
  `[(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2)]` (Target 2L achieved in **5 steps**).
* **Vacuum Cleaner Agent:**
  Cleaned both `A` and `B` in **3 actions** (`Suck` at A -> `Move` to B -> `Suck` at B).
* **Medical Diagnosis System:**
  Input: `['fever', 'headache', 'body ache']` -> Output: `Possible Seasonal Fever`.

## 4. Performance Analysis
| Problem | Approach | Time Complexity | Space Complexity | Execution Time |
| :--- | :--- | :--- | :--- | :--- |
| Water Jug Problem | BFS State Space | $O(V + E)$ | $O(V)$ | ~0.05 ms |
| Vacuum Cleaner Agent | Simple Reflex | $O(N)$ | $O(1)$ | ~0.01 ms |
| Medical Diagnosis | Rule Matching | $O(R \times S)$ | $O(R)$ | ~0.01 ms |

## 5. Learning Outcomes
* Understood **State Space Representation** (Initial State, Actions, Transition Model, and Goal State)[span_9](start_span)[span_9](end_span).
* Implemented **Production Rule Systems** and learned how AI agents make decisions based on rules and states[span_10](start_span)[span_10](end_span).
*
