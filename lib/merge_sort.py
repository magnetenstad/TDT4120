from merge import merge
from math import floor

def merge_sort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        return merge(A, p, q, r)
