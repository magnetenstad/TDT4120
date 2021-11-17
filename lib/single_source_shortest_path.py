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


def bellman_ford(G, w, s):
    initialize_single_source(G, s)
    for _ in range(len(G.V)):
        for u, v in G.E:
            relax(u, v, w)
    for u, v in G.E:
        if v.d > u.d + w[u][v]:
            return False
    return True


def dag_shortest_paths(G, w, s):
    initialize_single_source(G, s)
    u = topological_sort(G)
    while u != None:
        for v in G.Adj[u.key]:
            relax(u, v, w)
        u = u.next


def dijkstra(G, w, s):
    initialize_single_source(G, s)
    S = set()
    Q = G.V
    while Q:
        u = extract_min(Q) # TODO: implement extract_min
        S.add(u)
        for v in G.Adj[u]:
            relax(u, v, w)

