

class Graph:
    V = set()
    E = set()

class Vertex:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.rank = None

def connected_components(G):
    for v in G.V:
        make_set(v)
    for u, v in G.E:
        if find_set(u) != find_set(v):
            union(u, v)

def same_component(u, v):
    return find_set(u) == find_set(v)
    
def make_set(x):
    x.p = x
    x.rank = 0

def union(x, y):
    link(find_set(x), find_set(y))

def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def find_set(x):
    if x != x.p:
        x.p = find_set(x.p)
    return x.p

