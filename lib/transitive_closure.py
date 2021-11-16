
def transitive_closure(G):
    n = len(G.V)
    T = [None] * (n + 1)
    T[0] = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or (i, j) in G.E:
                T[0][i][j] = 1
            else:
                T[0][i][j] = 0
    for k in range(1, n + 1):
        T[k] = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                T[k][i][j] = T[k - 1][i][j] or T[k - 1][i][k] and T[k - 1][k][j]
    return T[n]


def transitive_closure_optimized(G):
    n = len(G.V)
    T = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or (i, j) in G.E:
                T[i][j] = 1
            else:
                T[i][j] = 0
    for k in range(1, n + 1):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or T[i][k] and T[k][j]
    return T
