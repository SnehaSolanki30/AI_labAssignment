import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement a Bayesian Belief Network (BBN) for a Home 
# Alarm System (Burglary & Earthquake -> Alarm -> JohnCalls 
# & MaryCalls) and compute exact joint and conditional 
# probabilities using Conditional Probability Tables (CPTs).
# ==========================================================

# Conditional Probability Tables (CPTs)
P_B = {True: 0.001, False: 0.999}   # P(Burglary)
P_E = {True: 0.002, False: 0.998}   # P(Earthquake)

# P(Alarm | Burglary, Earthquake)
P_A_given_BE = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

# P(JohnCalls | Alarm)
P_J_given_A = {True: 0.90, False: 0.05}

# P(MaryCalls | Alarm)
P_M_given_A = {True: 0.70, False: 0.01}


def joint_probability(b, e, a, j, m):
    """Computes P(B=b, E=e, A=a, J=j, M=m) using the chain rule of Bayesian Networks."""
    p_b = P_B[b]
    p_e = P_E[e]
    p_a = P_A_given_BE[(b, e)] if a else (1.0 - P_A_given_BE[(b, e)])
    p_j = P_J_given_A[a] if j else (1.0 - P_J_given_A[a])
    p_m = P_M_given_A[a] if m else (1.0 - P_M_given_A[a])
    return p_b * p_e * p_a * p_j * p_m


def infer_burglary_given_calls():
    """Computes P(Burglary=True | JohnCalls=True, MaryCalls=True) via enumeration."""
    start_time = time.time()

    # Sum over all hidden combinations of (Earthquake, Alarm)
    p_b_true_jm = sum(
        joint_probability(True, e, a, True, True)
        for e in [True, False]
        for a in [True, False]
    )
    p_b_false_jm = sum(
        joint_probability(False, e, a, True, True)
        for e in [True, False]
        for a in [True, False]
    )

    posterior_burglary = p_b_true_jm / (p_b_true_jm + p_b_false_jm)
    exec_time = (time.time() - start_time) * 1000
    return posterior_burglary, exec_time


if __name__ == "__main__":
    # 1. Joint probability of specific event: Alarm rings, John & Mary call, no Burglary/Earthquake
    jp = joint_probability(b=False, e=False, a=True, j=True, m=True)

    # 2. Posterior inference: Probability of Burglary given both John and Mary called
    prob_burglary, elapsed = infer_burglary_given_calls()

    print("=== Bayesian Belief Network (Alarm System) ===")
    print(f"Joint Probability P(~B, ~E, A, J, M)         : {jp:.8f}")
    print(f"Posterior P(Burglary=True | John & Mary Call): {prob_burglary * 100:.2f}%")
    print(f"Execution Time                               : {elapsed:.4f} ms")
