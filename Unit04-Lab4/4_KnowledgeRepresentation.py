import time

# ==========================================
# 1. SEMANTIC NETWORK REPRESENTATION
# ==========================================
class SemanticNetwork:
    """Represents knowledge as a graph of nodes and directed relationships."""
    def __init__(self):
        self.edges = {}  # {entity: [(relation, target), ...]}

    def add_relation(self, subject, relation, obj):
        if subject not in self.edges:
            self.edges[subject] = []
        self.edges[subject].append((relation, obj))

    def query(self, subject, relation=None):
        """Retrieves direct and inherited ('is_a') properties."""
        results = []
        visited = set()

        def dfs(curr):
            if curr in visited or curr not in self.edges:
                return
            visited.add(curr)
            for rel, target in self.edges[curr]:
                if relation is None or rel == relation:
                    results.append((curr, rel, target))
                if rel == "is_a":
                    dfs(target)

        dfs(subject)
        return results


# ==========================================
# 2. FRAME-BASED KNOWLEDGE REPRESENTATION
# ==========================================
class Frame:
    """Represents structured object knowledge with slots and inheritance."""
    def __init__(self, name, parent=None, slots=None):
        self.name = name
        self.parent = parent
        self.slots = slots if slots else {}

    def get_slot(self, key):
        if key in self.slots:
            return self.slots[key]
        if self.parent:
            return self.parent.get_slot(key)
        return None


# ==========================================
# 3. LOGICAL RULE ENGINE (Forward Chaining)
# ==========================================
class RuleEngine:
    """Forward-chaining inference engine for University Knowledge Base."""
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, conditions, conclusion):
        self.rules.append((set(conditions), conclusion))

    def infer(self):
        added = True
        while added:
            added = False
            for conditions, conclusion in self.rules:
                if conditions.issubset(self.facts) and conclusion not in self.facts:
                    self.facts.add(conclusion)
                    added = True
        return self.facts


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    start_time = time.time()

    # 1. Semantic Network Demo (University Knowledge Base)
    print("=== 1. Semantic Network (University Knowledge Base) ===")
    sn = SemanticNetwork()
    sn.add_relation("Sneha", "is_a", "MCA_Student")
    sn.add_relation("MCA_Student", "is_a", "Student")
    sn.add_relation("MCA_Student", "studies_at", "IIPS_DAVV")
    sn.add_relation("Student", "has_access_to", "University_Library")

    inferred_props = sn.query("Sneha")
    for subj, rel, obj in inferred_props:
        print(f"  {subj} --[{rel}]--> {obj}")

    # 2. Frame Representation Demo
    print("\n=== 2. Frame Representation ===")
    university_course = Frame("Course", slots={"University": "DAVV", "Mode": "Regular"})
    ai_course = Frame("IC-709D", parent=university_course, slots={"Title": "AI Lab", "Credits": 4})
    print(f"  Course: {ai_course.name} | Title: {ai_course.get_slot('Title')} | University (Inherited): {ai_course.get_slot('University')}")

    # 3. Logical Rule Engine Demo
    print("\n=== 3. Logical Rule Engine (Forward Chaining) ===")
    engine = RuleEngine()
    engine.add_fact("enrolled_in_MCA")
    engine.add_fact("passed_sem5")
    engine.add_fact("attendance_above_75")

    engine.add_rule(["enrolled_in_MCA", "passed_sem5"], "eligible_for_sem6")
    engine.add_rule(["eligible_for_sem6", "attendance_above_75"], "eligible_for_final_exam")

    all_facts = engine.infer()
    exec_time = (time.time() - start_time) * 1000
    print("  Inferred Facts:", sorted(all_facts))
    print(f"\nTotal Execution Time: {exec_time:.4f} ms")
