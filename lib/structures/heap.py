from math import floor


class Heap(list):
    heap_size = 0


def parent(i):
    return floor(i / 2)

def left(i):
    return 2 * i + 1 # 2 * i, if 1-indexed

def right(i):
    return 2 * i + 2  # 2 * i + 1, if 1-indexed


# MAX-HEAP functions:

def max_heapify(A, i):
    """
    MAX-HEAPIFY
    Time complexity: O(lg n) / O(h)
    """
    l = left(i)
    r = right(i)
    if l < A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)

def build_max_heap(A):
    """
    BUILD-MAX-HEAP
    Time complexity: O(n lg n)
    """
    A.heap_size = len(A)
    for i in range(floor(len(A) / 2), -1, -1):
        max_heapify(A, i)

def heap_maximum(A):
    return A[0]

def heap_extract_max(A):
    """
    HEAP-EXTRACT-MAX
    Time complexity: O(lg n)
    """
    if A.heap_size < 0:
        print("ERROR: heap underflow")
    max_ = A[0]
    A[0] = A[A.heap_size - 1]
    A.heap_size -= 1
    max_heapify(A, 1)
    return max_

def heap_increase_key(A, i, key):
    """
    HEAP-INCREASE-KEY
    Time complexity: O(lg n)
    """
    if key < A[i]:
        print("ERROR: new key is smaller than current key")
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)

def max_heap_insert(A, key):
    A.heap_size += 1
    A[A.heap_size - 1] = -float('inf')
    heap_increase_key(A, A.heap_size - 1, key)



# TODO: MIN-HEAP functions:

if __name__ == '__main__':
    A = Heap([1, 6, 2, 5, 4, 2, 5, 2, 1, 4, 9, 7, 8])
    build_max_heap(A)
    print(A)