
def extend_shortest_paths(L, W):
    n = len(L)
    l = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            l[i][j] = float('inf')
            for k in range(n):
                l[i][j] = min(l[i][j], l[i][k] + W[k][j])
    return l


def print_all_pairs_shortest_path(Pi, i, j):
    if i == j:
        print(i)
    elif Pi[i][j] == None:
        print(f"No path from {i} to {j} exists.")
    else:
        print_all_pairs_shortest_path(Pi, i, Pi[i][j])
        print(j)

def slow_all_pairs_shortest_paths(W):
    n = len(W)
    L = [None] * (n)
    L[0] = W
    for m in range(1, n):
        L[m] = [[None] * n for _ in range(n)]
        L[m] = extend_shortest_paths(L[m - 1], W)
    return L[n - 1]

def faster_all_pairs_shortest_paths(W):
    n = len(W)
    L = [None] * (n)
    L[0] = W
    m = 1
    while m < n - 1:
        L[2 * m] = [[None] * n for _ in range(n)]
        L[2 * m] = extend_shortest_paths(L[m], L[m])
        m *= 2
    return L[m - 1]


def floyd_warshall(W):
    n = len(W)
    D = [None] * (n + 1)
    D[0] = W
    for k in range(1, n + 1):
        D[k] = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                D[k][i][j] = min(D[k - 1][i][j], \
                    D[k - 1][i][k] + D[k - 1][k][j])
    return D[n]

def floyd_warshall_optimized(W):
    n = len(W)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                W[i][j] = min(W[i][j], W[i][k] + W[k][j])


def johnson(G, w):
    pass # TODO: implement johnson