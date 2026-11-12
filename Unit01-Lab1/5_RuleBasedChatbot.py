def rule_based_chatbot(user_input):
    """Simple Rule-Based Academic Assistant Chatbot."""
    msg = user_input.lower().strip()
    rules = {
        "hello": "Hello! I am your AI Lab Assistant. How can I help you today?",
        "subject": "This lab is IC-709D: Artificial Intelligence Lab for MCA VI Semester.",
        "water jug": "The Water Jug problem demonstrates State Space Search using production rules.",
        "algorithms": "In AI, we use BFS, DFS, Hill Climbing, Best-First Search, and A*.",
        "bye": "Goodbye! Keep practicing AI problem formulation."
    }
    for keyword, response in rules.items():
        if keyword in msg:
            return response
    return "Sorry, I don't have a rule for that query yet."

if __name__ == "__main__":
    queries = ["Hello!", "Tell me about subject", "What is water jug?"]
    for q in queries:
        print(f"User: {q} -> Bot: {rule_based_chatbot(q)}")
