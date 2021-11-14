
def counting_sort(A, B, k, d):
    """
    COUNTING-SORT

    Time Complexity: Theta(n + k)
    Space Complecity: Theta(k)

    In place: False
    Stable: True
    """
    C = [0] * k
    for v in A:
        C[ord(v[d])] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A) - 1, -1, -1):
        v = A[i]
        B[C[ord(v[d])]-1] = v
        C[ord(v[d])] -= 1


def radix_sort(A, d):
    """
    RADIX-SORT
    (using COUNTING-SORT)

    Time Complexity: Theta(d(n + k))
    Space Complecity: Theta(n + k)

    In place: False
    Stable: True
    """
    B = [None] * len(A)
    k = (ord(max(c for word in A for c in word)) + 1) \
        if len(A) and d else 0
    for i in range(d-1,-1,-1):
        counting_sort(A, B, k, i)
        A, B = B, A
    return A

if __name__ == '__main__':
    from tests import test_algorithm, get_radix_sort_problem_instances
    test_algorithm(radix_sort, get_radix_sort_problem_instances())
