# Lab 4: Knowledge Representation & Logical Reasoning

## 1. Aim / Problem Statement
To implement structured AI knowledge representation schemes and logical reasoning using a University Knowledge Base[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span):
1. **Semantic Network Construction** with `is_a` property inheritance[span_7](start_span)[span_7](end_span).
2. **Frame Representation** with hierarchical slots and default values[span_8](start_span)[span_8](end_span).
3. **Logical Rule Engine** using Forward Chaining inference[span_9](start_span)[span_9](end_span).

## 2. Algorithm
* **Semantic Network:** Represents entities as graph nodes and relationships as directed edges. Uses Depth-First Search (DFS) along `is_a` links to infer inherited properties.
* **Frame Representation:** Models concepts as objects (`Frame`) containing attribute-value pairs (`slots`) and delegates missing slot lookups to parent frames.
* **Logical Rule Engine:** Iteratively checks `IF-THEN` rules against known facts (`Forward Chaining`) and adds new inferred conclusions until no more rules fire.

## 3. Results / Output
* **Semantic Network Query (`Sneha`):**
  * `Sneha --[is_a]--> MCA_Student`
  * `MCA_Student --[studies_at]--> IIPS_DAVV`
  * `Student --[has_access_to]--> University_Library` (Inherited)
* **Frame Lookup (`IC-709D`):**
  * Retrieved local slot `Title: AI Lab` and inherited slot `University: DAVV`.
* **Forward Chaining Inference:**
  * Derived `eligible_for_sem6` and `eligible_for_final_exam` from initial student facts.

## 4. Performance Analysis
| Representation Scheme | Structure | Strength | Limitation | Execution Time |
| :--- | :--- | :--- | :--- | :--- |
| Semantic Networks | Graph (Nodes & Edges) | Intuitive visual & inheritance hierarchy | Difficult to represent complex logic/negation | ~0.02 ms |
| Frames | Object-Oriented Slots | Modular, supports default values & inheritance | Rigid schema for unstructured facts | ~0.01 ms |
| Rule-Based Systems | `IF-THEN` Productions | Clear modular logic & forward/backward chaining | Conflict resolution needed for large rule bases | ~0.02 ms |

## 5. Learning Outcomes
* Implemented **Semantic Networks**, **Frames**, and **Rule-Based Logical Inference** in Python[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).
* Compared different knowledge representation techniques in terms of expressiveness, inheritance, and reasoning efficiency[span_12](start_span)[span_12](end_span).
*
