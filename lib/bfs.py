from structures.queue import Queue, enqueue, dequeue

def bfs(G, s):
    for u in G.V - set(s):
        u.color = "white"
        u.d = float('inf')
        u.pi = None
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = Queue()
    enqueue(Q, s)
    while Q:
        u = dequeue(Q)
        for v in G.Adj[u]:
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.pi = u
                enqueue(Q, v)
        u.color = "black"
    