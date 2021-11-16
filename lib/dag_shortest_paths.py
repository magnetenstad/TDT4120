from topological_sort import topological_sort


def initialize_single_source(G, s):
    for v in G.V:
        v.d = float('inf')
        v.pi = None
    s.d = 0


def relax(u, v, w):
    if v.d > u.d + w[u][v]:
        v.d = u.d + w[u][v]
        v.pi = u


def dag_shortest_paths(G, w, s):
    initialize_single_source(G, s)
    u = topological_sort(G)
    while u != None:
        for v in G.Adj[u.key]:
            relax(u, v, w)
        u = u.next
    