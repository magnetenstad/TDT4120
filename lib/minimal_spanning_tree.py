from structures.disjunct_set import make_set, find_set, union
from structures.binary_heap import build_min_heap, heap_extract_min 

# GENERIC-MST(G, w)
# 1 A = Ø
# 2 while A does not form a spanning tree
# 3     find an edge (u, v) that is safe for A
# 4     A = A U {(u, v)}
# 5 return A


def mst_kruskal(G, w):
    A = set()
    for v in G.V:
        make_set(v)
    edges = sorted(G.E, key=lambda edge: w[edge[0]][edge[1]])
    for u, v in edges:
        if find_set(u) != find_set(v):
            A.add((u, v))
            union(u, v)


def mst_prim(G, w, r):
    for u in G.V:
        u.key = float('inf')
        u.pi = None
    r.key = 0
    Q = build_min_heap(G.V.copy())
    while Q:
        u = heap_extract_min(Q)
        for v in G.Adj[u]:
            if v in Q and w[u][v] < v.key:
                v.pi = u
                v.key = w[u][v]
