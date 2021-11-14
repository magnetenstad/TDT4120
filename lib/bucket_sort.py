from math import floor
if __name__ == '__main__':
    from insertion_sort import insertion_sort
else:
    from lib.insertion_sort import insertion_sort


def bucket_sort(A):
    """
    BUCKET-SORT

    Time Complexity:
        Worst case: Theta(n^2) if many elements are placed in the same bucket
        Average case: Theta(n)
        Best case: Theta(n)
    Space Complecity: Theta(n)

    In place: False
    Stable: True
    """
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):
        B[floor(n * A[i])].append(A[i])

    for j in range(n):
        insertion_sort(B[j])

    return [value for bucket in B for value in bucket]


if __name__ == '__main__':
    from tests import test_algorithm, get_bucket_sort_problem_instances
    test_algorithm(bucket_sort, get_bucket_sort_problem_instances())
