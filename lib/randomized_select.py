if __name__ == '__main__':
    from quicksort import randomized_partition
else:
    from lib.quicksort import randomized_partition


def randomized_select(A, p, r, i):
    """
    RANDOMIZED-SELECT

    Returns the ith smallest element of the array A[p..r].

    Time Complexity:
        Worst case: Theta(n^2)
        Average case: Theta(n)
        Best case: Theta(n)
    Space Complecity: Theta(1)

    In place: True
    """
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


if __name__ == '__main__':
    from tests import test_algorithm, get_randomized_select_problem_instances
    test_algorithm(randomized_select, get_randomized_select_problem_instances())
    