import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement Bayes' Theorem to calculate the posterior 
# probability of a disease given a positive diagnostic test 
# result, accounting for prior probability, sensitivity, 
# and false positive rate.
# ==========================================================

def bayes_theorem(prior_disease, sensitivity, false_positive_rate):
    """
    Computes P(Disease | Positive Test) using Bayes' Theorem:
    P(D|T+) = [P(T+|D) * P(D)] / P(T+)
    """
    start_time = time.time()

    prior_healthy = 1.0 - prior_disease
    # Total probability of testing positive: P(T+)
    p_positive = (sensitivity * prior_disease) + (false_positive_rate * prior_healthy)

    # Posterior probability: P(D | T+)
    posterior = (sensitivity * prior_disease) / p_positive
    exec_time = (time.time() - start_time) * 1000

    return posterior, p_positive, exec_time


if __name__ == "__main__":
    # Given Probabilities
    p_disease = 0.01          # 1% of population has the disease: P(D)
    p_pos_given_d = 0.95      # 95% sensitivity (True Positive Rate): P(T+ | D)
    p_pos_given_no_d = 0.05   # 5% false positive rate: P(T+ | ~D)

    posterior_prob, total_pos_prob, elapsed = bayes_theorem(
        p_disease, p_pos_given_d, p_pos_given_no_d
    )

    print("=== Probabilistic Reasoning: Bayes' Theorem ===")
    print(f"Prior Probability of Disease P(D)         : {p_disease * 100:.2f}%")
    print(f"Test Sensitivity P(T+ | D)                : {p_pos_given_d * 100:.2f}%")
    print(f"False Positive Rate P(T+ | ~D)            : {p_pos_given_no_d * 100:.2f}%")
    print(f"Total Probability of Positive Test P(T+)  : {total_pos_prob * 100:.2f}%")
    print(f"Posterior Probability P(D | T+)           : {posterior_prob * 100:.2f}%")
    print(f"Execution Time                            : {elapsed:.4f} ms")
