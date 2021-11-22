if __name__ == '__main__':
    from structures.binary_heap import build_max_heap, max_heapify
else:
    from lib.structures.binary_heap import build_max_heap, max_heapify


def heapsort(A):
    """
    HEAPSORT

    Time Complexity: O(n lg n)
    Space Complecity: Theta(1)

    In place: True
    Stable: False
    """
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        A.heap_size -= 1
        max_heapify(A, 0)


if __name__ == '__main__':
    from tests import test_algorithm, get_heapsort_problem_instances
    test_algorithm(heapsort, get_heapsort_problem_instances(), in_place=True)
