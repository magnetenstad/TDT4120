from lib.structures.binary_heap import build_min_heap, heap_extract_min, \
    min_heap_insert


class Node:
    freq = 0


def huffman(C):
    n = len(C)
    Q = build_min_heap(C.copy())
    for _ in range(n - 1):
        z = Node()
        x = heap_extract_min(Q)
        y = heap_extract_min(Q)
        z.freq = x.freq + y.freq
        min_heap_insert(Q, z)
    return heap_extract_min(Q)
