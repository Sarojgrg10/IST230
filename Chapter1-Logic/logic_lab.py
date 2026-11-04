
# ZYBOOKS SECTION 1.1: BASIC OPERATIONS
def negation(p: bool) -> bool:
    return not p
def conjunction(p: bool, q: bool) -> bool:
    return p and q
def disjunction(p: bool, q: bool) -> bool:
    return p or q
def exclusive_or(p: bool, q: bool) -> bool:
    return p != q

# ZYBOOKS SECTION 1.3: CONDITIONAL OPERATIONS
def conditional(p: bool, q: bool) -> bool:
    return not p or q
def biconditional(p: bool, q: bool) -> bool:
    return p == q

# AUTOMATED TRUTH TABLE GENERATOR
def run_truth_table_generator():
    print(f"{'p':<6} | {'q':<6} | {'¬p':<6} | {'p ∧ q':<6} | {'p → q':<12} | {'q → p (Conv)':<13}")
    print("-" * 60)
    combinations = [(True, True), (True, False), (False, True), (False, False)]

    for p, q in combinations:
        not_p = negation(p)
        and_op = conjunction(p, q)
        imp_op = conditional(p, q)
        conv_op = conditional(q, p)

        print(f"{str(p):<6} | {str(q):<6} | {str(not_p):<6} | {str(and_op):<6} | {str(imp_op):<12} | {str(conv_op):<13}")


if __name__ == "__main__":
    print("IST 230 Lab - Chapter 1 Evaluation Matrix")
    run_truth_table_generator()
