import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement a Propositional Logic Forward-Chaining Inference 
# Engine that derives new logical facts from a given Knowledge 
# Base (KB) of facts and IF-THEN rules.
# ==========================================================

def forward_chaining(facts, rules, query):
    """Derives new facts using Forward Chaining until the query is proven or no new facts emerge."""
    start_time = time.time()
    inferred = set(facts)
    added = True

    while added:
        added = False
        for premises, conclusion in rules:
            # If all premises are true in our known facts, infer the conclusion
            if premises.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                print(f"Rule Applied: {set(premises)} => {conclusion}")
                added = True
                if conclusion == query:
                    exec_time = (time.time() - start_time) * 1000
                    return True, inferred, exec_time

    exec_time = (time.time() - start_time) * 1000
    return (query in inferred), inferred, exec_time


if __name__ == "__main__":
    # Initial Known Facts
    known_facts = {"has_fur", "lays_eggs", "has_bill"}

    # Knowledge Base Rules: (Set of Conditions, Inferred Fact)
    kb_rules = [
        ({"has_fur"}, "is_mammal"),
        ({"has_feathers"}, "is_bird"),
        ({"is_mammal", "lays_eggs", "has_bill"}, "is_platypus"),
        ({"is_bird", "cannot_fly"}, "is_penguin")
    ]

    goal_query = "is_platypus"

    print("=== Propositional Logic Forward-Chaining Engine ===")
    print("Initial Facts:", known_facts)
    print("Query to Prove:", goal_query, "\n")

    is_proven, final_facts, elapsed = forward_chaining(known_facts, kb_rules, goal_query)

    print(f"\nQuery '{goal_query}' Proven? : {is_proven}")
    print(f"Final Knowledge Base       : {final_facts}")
    print(f"Execution Time             : {elapsed:.4f} ms")
