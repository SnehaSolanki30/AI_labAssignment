import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement a Hidden Markov Model (HMM) using the Viterbi 
# Algorithm to infer the most likely sequence of hidden 
# weather states ('Rainy', 'Sunny') from a sequence of 
# observed activities ('Walk', 'Shop', 'Clean').
# ==========================================================

def viterbi_algorithm(observations, states, start_prob, trans_prob, emit_prob):
    """Finds the most probable sequence of hidden states using Viterbi decoding."""
    start_time = time.time()
    V = [{}]
    path = {}

    # 1. Initialization step (t = 0)
    for state in states:
        V[0][state] = start_prob[state] * emit_prob[state][observations[0]]
        path[state] = [state]

    # 2. Recursion step (t = 1 to T-1)
    for t in range(1, len(observations)):
        V.append({})
        new_path = {}

        for curr_state in states:
            (max_prob, prev_best_state) = max(
                (V[t - 1][prev_state] * trans_prob[prev_state][curr_state] * emit_prob[curr_state][observations[t]], prev_state)
                for prev_state in states
            )
            V[t][curr_state] = max_prob
            new_path[curr_state] = path[prev_best_state] + [curr_state]

        path = new_path
