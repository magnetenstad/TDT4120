
def dfs(G):
    for u in G.V:
        u.color == "white"
        u.pi = None
    time = 0
    for u in G.V:
        if u.color == "white":
            dfs_visit(G, u, time)
    
def dfs_visit(G, u, time):
    time += 1
    u.d = time
    u.color = "gray"
    for v in G.Adj[u]:
        if v.color == "white":
            v.pi = u
            dfs_visit(G, v, time)
    u.color = "black"
    time += 1
    u.f = time

