
def bubble_sort(A):
    """
    BUBBLE-SORT

    Time Complexity:
        Worst case: Theta(n^2) if input is in reverse order
        Average case: Theta(n^2)
        Best case: Theta(n) if input is already sorted
    Space Complecity: Theta(1)

    In place: True
    Stable: True
    """
    for i in range(0, len(A)):
        swapped = False
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                swapped = True
        if not swapped:
            break
    

if __name__ == '__main__':
    from tests import test_algorithm, get_sort_problem_instances
    test_algorithm(bubble_sort, get_sort_problem_instances(), in_place=True)
