# Lab 1: AI Problem Formulation & Production Systems

## 1. Aim / Problem Statement
To understand AI problem formulation, state-space representation, and implement rule-based production systems across 5 standalone Python programs:
1. **Water Jug Problem (`1_WaterJugProblem.py`):** Measure 2 liters of water using a 4-liter and a 3-liter jug.
2. **Missionaries and Cannibals (`2_MissionariesCannibals.py`):** Safely transport 3 missionaries and 3 cannibals across a river without outnumbering missionaries on either bank.
3. **Vacuum Cleaner Agent (`3_VacuumCleanerAgent.py`):** Clean a two-location environment (`A` and `B`) using a simple reflex agent.
4. **Rule-Based Medical Diagnosis System (`4_MedicalDiagnosisSystem.py`):** Identify possible illnesses based on patient symptoms using `IF-THEN` production rules.
5. **Rule-Based AI Chatbot (`5_RuleBasedChatbot.py`):** Respond to user queries using pattern-matching production rules.

## 2. Algorithm
* **Water Jug & Missionaries-Cannibals:** Uses Breadth-First Search (BFS) with a `visited` set to explore valid state transitions and guarantee the shortest solution path.
* **Vacuum Cleaner Agent:** Uses a simple condition-action rule (`IF status == Dirty THEN Suck ELSE Move`) until all rooms are clean.
* **Medical Diagnosis & Chatbot:** Matches user inputs or symptom sets against predefined `IF-THEN` rules and keywords.

## 3. How to Run
```bash
python 1_WaterJugProblem.py
python 2_MissionariesCannibals.py
python 3_VacuumCleanerAgent.py
python 4_MedicalDiagnosisSystem.py
python 5_RuleBasedChatbot.py
