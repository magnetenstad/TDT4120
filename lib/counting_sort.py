
def counting_sort(A, B, k):
    """
    COUNTING-SORT

    Time Complexity: Theta(n + k)
    Space Complecity: Theta(k)

    In place: False
    Stable: True
    """
    C = [0] * k
    for i in A:
        C[i] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A) - 1, -1, -1):
        v = A[i]
        B[C[v]-1] = v
        C[v] -= 1


if __name__ == '__main__':
    from tests import test_algorithm, get_counting_sort_problem_instances
    test_algorithm(counting_sort, get_counting_sort_problem_instances(), \
        in_place=True, output=1)
