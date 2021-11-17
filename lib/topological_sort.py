from structures.linked_list import LinkedList, LinkedListElement, list_insert

def topological_sort(G):
    global L
    L = LinkedList()
    ts_dfs(G)
    return L

def ts_dfs(G):
    global time
    for u in G.V:
        u.color == "white"
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == "white":
            ts_dfs_visit(G, u)
    
def ts_dfs_visit(G, u):
    global time, L
    time += 1
    u.d = time
    u.color = "gray"
    for v in G.Adj[u]:
        if v.color == "white":
            v.pi = u
            ts_dfs_visit(G, v)
    u.color = "black"
    time += 1
    u.f = time
    list_insert(L, LinkedListElement(u))
