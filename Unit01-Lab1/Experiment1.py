import time
from collections import deque

# ==========================================
# 1. WATER JUG PROBLEM (Using BFS)
# ==========================================
def water_jug_solver(jug1_capacity, jug2_capacity, target):
    """Solves the Water Jug Problem using Breadth-First Search (BFS)."""
    start_time = time.time()
    visited = set()
    queue = deque([((0, 0), [(0, 0)])])

    while queue:
        (jug1, jug2), path = queue.popleft()

        if jug1 == target or jug2 == target:
            exec_time = (time.time() - start_time) * 1000
            return path, exec_time

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Production Rules
        next_states = [
            (jug1_capacity, jug2),  # Fill Jug 1
            (jug1, jug2_capacity),  # Fill Jug 2
            (0, jug2),              # Empty Jug 1
            (jug1, 0),              # Empty Jug 2
            # Pour Jug 1 into Jug 2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug 2 into Jug 1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))

    return None, 0


# ==========================================
# 2. VACUUM CLEANER AGENT (Reflex Agent)
# ==========================================
def vacuum_cleaner_agent(environment, start_location):
    """Simulates a Simple Reflex Vacuum Cleaner Agent."""
    location = start_location
    actions = []
    cost = 0

    for _ in range(len(environment) * 2):
        if all(status == "Clean" for status in environment.values()):
            break

        if environment[location] == "Dirty":
            actions.append(f"Location {location} is Dirty -> Action: SUCK")
            environment[location] = "Clean"
            cost += 1
        else:
            next_loc = "B" if location == "A" else "A"
            actions.append(f"Location {location} is Clean -> Action: MOVE to {next_loc}")
            location = next_loc
            cost += 1

    return actions, cost, environment


# ==========================================
# 3. RULE-BASED MEDICAL DIAGNOSIS SYSTEM
# ==========================================
def medical_diagnosis(symptoms):
    """Production Rule-Based System for basic medical diagnosis."""
    symptoms = {s.lower().strip() for s in symptoms}

    rules = [
        ({"fever", "cough", "fatigue"}, "Possible Viral Infection / Flu"),
        ({"fever", "headache", "body ache"}, "Possible Seasonal Fever"),
        ({"sneezing", "runny nose", "itchy eyes"}, "Possible Allergic Rhinitis"),
        ({"headache", "nausea"}, "Possible Migraine"),
        ({"stomach pain", "acidity"}, "Possible Gastritis")
    ]

    for condition_set, diagnosis in rules:
        if condition_set.issubset(symptoms):
            return diagnosis

    return "Symptoms inconclusive. Please consult a doctor."


# ==========================================
# MAIN PROGRAM EXECUTION
# ==========================================
if __name__ == "__main__":
    print("=== 1. Water Jug Problem (4L, 3L -> Target: 2L) ===")
    path, elapsed = water_jug_solver(4, 3, 2)
    print("Solution Path:", path)
    print(f"Total Steps: {len(path) - 1} | Execution Time: {elapsed:.4f} ms\n")

    print("=== 2. Vacuum Cleaner Agent ===")
    room_env = {"A": "Dirty", "B": "Dirty"}
    steps, total_cost, final_env = vacuum_cleaner_agent(room_env, "A")
    for step in steps:
        print(step)
    print(f"Final State: {final_env} | Total Cost: {total_cost}\n")

    print("=== 3. Rule-Based Medical Diagnosis ===")
    patient_symptoms = ["fever", "headache", "body ache"]
    print("Symptoms:", patient_symptoms)
    print("Diagnosis:", medical_diagnosis(patient_symptoms))
