
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def quicksort(A, p, r):
    """
    QUICKSORT

    Time Complexity:
        Worst case: Theta(n^2) if input is sorted
        Average case: Theta(n lg n)
        Best case: Theta(n lg n)
    Space Complecity: Theta(1)

    In place: True
    Stable: False
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


from random import randint
def randomized_partition(A, p, r):
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    """
    RANDOMIZED-QUICKSORT

    Time Complexity:
        Expected worst case: Theta(n lg n)
        Average case: Theta(n lg n)
        Best case: Theta(n lg n)
    Space Complecity: Theta(1)

    In place: True
    Stable: False
    """
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)



if __name__ == '__main__':
    from tests import test_algorithm, get_merge_sort_problem_instances
    test_algorithm(quicksort, get_merge_sort_problem_instances(), in_place=True)
    test_algorithm(randomized_quicksort, \
        get_merge_sort_problem_instances(), in_place=True)
