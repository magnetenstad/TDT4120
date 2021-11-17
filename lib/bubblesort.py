
def bubblesort(A):
    """
    BUBBLESORT

    Time Complexity:
        Worst case: Theta(n^2)
        Average case: Theta(n^2)
        Best case: Theta(n^2)
    Space Complecity: Theta(1)

    In place: True
    Stable: True
    """
    for i in range(0, len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
    
    
if __name__ == '__main__':
    from tests import test_algorithm, get_sort_problem_instances
    test_algorithm(bubblesort, get_sort_problem_instances(), in_place=True)
