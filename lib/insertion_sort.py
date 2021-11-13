
def insertion_sort(A):
    """
    INSERTION-SORT

    Time Complexity:
        Worst case: Theta(n^2) if input is in reverse order
        Average case: Theta(n^2)
        Best case: Theta(n) if input is already sorted
    Space Complecity: Theta(1)

    In place: True
    Stable: True

    Loop invariant: At the start of each iteration, the subarray
    A[1 .. j - 1] consists of the elements originally in A[1 .. j - 1],
    but in sorted order.
    """
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[j] into the sorted sequence A[0 .. j - 1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


if __name__ == '__main__':
    from tests import test_algorithm, get_sort_problem_instances
    test_algorithm(insertion_sort, get_sort_problem_instances(), in_place=True)
