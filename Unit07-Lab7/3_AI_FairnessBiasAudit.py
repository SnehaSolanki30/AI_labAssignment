import time

# ==========================================================
# PROBLEM STATEMENT:
# Implement an AI Ethics & Fairness Audit tool that evaluates 
# an automated loan-approval model across demographic groups 
# using the Demographic Parity Ratio (80% / Four-Fifths Rule) 
# to detect algorithmic bias.
# ==========================================================

def audit_model_fairness(predictions):
    """Calculates approval rates per group and checks the 80% Fairness Rule."""
    start_time = time.time()
    group_stats = {}

    for group, approved in predictions:
        if group not in group_stats:
            group_stats[group] = {"total": 0, "approved": 0}
        group_stats[group]["total"] += 1
        if approved == 1:
            group_stats[group]["approved"] += 1

    approval_rates = {
        grp: (stats["approved"] / stats["total"])
        for grp, stats in group_stats.items()
    }

    max_rate = max(approval_rates.values())
    min_rate = min(approval_rates.values())
    disparate_impact_ratio = min_rate / max_rate if max_rate > 0 else 1.0
    is_fair = disparate_impact_ratio >= 0.80

    exec_time = (time.time() - start_time) * 1000
    return approval_rates, disparate_impact_ratio, is_fair, exec_time


if __name__ == "__main__":
    # Sample AI Loan Approval Decisions: (Demographic_Group, Approved_1_or_0)
    loan_decisions = [
        ("Group_A", 1), ("Group_A", 1), ("Group_A", 1), ("Group_A", 1), ("Group_A", 0),
        ("Group_B", 1), ("Group_B", 1), ("Group_B", 0), ("Group_B", 0), ("Group_B", 0)
    ]

    rates, ratio, passed, elapsed = audit_model_fairness(loan_decisions)

    print("=== AI Ethics: Algorithmic Fairness & Bias Audit ===")
    for grp, rate in rates.items():
        print(f"  {grp} Approval Rate : {rate * 100:.1f}%")

    print(f"\nDisparate Impact Ratio   : {ratio:.2f} (Threshold >= 0.80)")
    print(f"Fairness Audit Status    : {'PASSED (Fair)' if passed else 'FAILED (Bias Detected)'}")
    print(f"Execution Time           : {elapsed:.4f} ms")
