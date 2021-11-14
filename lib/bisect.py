from math import floor


def bisect(A, p, r, v):
    """
    BISECT (BINARY-SEARCH)

    Time Complexity:
        Worst case: Theta(1) if v is in the middle
        Average case: Theta(lg n)
        Best case: Theta(lg n)
    Space Complecity: Theta(1)
    """
    if p <= r:
        q = floor((p + r) / 2)
        if v == A[q]:
            return q
        elif v < A[q]:
            return bisect(A, p, q - 1, v)
        else:
            return bisect(A, q + 1, r, v)
    else:
        return None


def iterative_bisect(A, p, r, v):
    """
    ITERATIVE-BISECT (BINARY-SEARCH)

    Time Complexity:
        Worst case: Theta(1) if v is in the middle
        Average case: Theta(lg n)
        Best case: Theta(lg n)
    Space Complecity: Theta(1)
    """
    while p <= r:
        q = floor((p + r) / 2)
        if v == A[q]:
            return q
        elif v < A[q]:
            r = q - 1
        else:
            p = q + 1
    return None


if __name__ == '__main__':
    from tests import test_algorithm, get_bisect_problem_instances
    test_algorithm(bisect, get_bisect_problem_instances())
    test_algorithm(iterative_bisect, get_bisect_problem_instances())