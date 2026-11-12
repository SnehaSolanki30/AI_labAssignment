import time
import random

# ==========================================================
# PROBLEM STATEMENT:
# Implement the Q-Learning Reinforcement Learning algorithm 
# to train an autonomous agent to navigate a 1D Grid World 
# (States 0 to 4) and reach the Goal State (4) with maximum 
# cumulative reward.
# ==========================================================

def train_q_learning(num_states=5, episodes=200, alpha=0.1, gamma=0.9, epsilon=0.2):
    """Trains a Q-Table using the Bellman Equation for Q-Learning."""
    start_time = time.time()
    actions = ["LEFT", "RIGHT"]
    q_table = {state: {"LEFT": 0.0, "RIGHT": 0.0} for state in range(num_states)}
    goal_state = num_states - 1

    for _ in range(episodes):
        state = 0  # Start at leftmost cell

        while state != goal_state:
            # Epsilon-greedy action selection
            if random.random() < epsilon:
                action = random.choice(actions)
            else:
                action = max(q_table[state], key=q_table[state].get)

            # Environment step
            if action == "RIGHT":
                next_state = min(goal_state, state + 1)
            else:
                next_state = max(0, state - 1)

            reward = 100 if next_state == goal_state else -1

            # Q-Learning Update Rule
            best_next_q = max(q_table[next_state].values())
            q_table[state][action] += alpha * (
                reward + gamma * best_next_q - q_table[state][action]
            )

            state = next_state

    exec_time = (time.time() - start_time) * 1000
    return q_table, exec_time


if __name__ == "__main__":
    random.seed(42)
    learned_q_table, elapsed = train_q_learning()

    print("=== Reinforcement Learning: Q-Learning Grid World ===")
    print("Learned Q-Table (State -> Action Values):")
    for state, q_vals in learned_q_table.items():
        print(f"  State {state}: LEFT = {q_vals['LEFT']:6.2f} | RIGHT = {q_vals['RIGHT']:6.2f}")

    # Test optimal policy from State 0
    curr = 0
    path = [curr]
    while curr != 4:
        best_act = max(learned_q_table[curr], key=learned_q_table[curr].get)
        curr = curr + 1 if best_act == "RIGHT" else curr - 1
        path.append(curr)

    print(f"\nOptimal Learned Path : {' -> '.join(map(str, path))}")
    print(f"Training Time        : {elapsed:.4f} ms")
