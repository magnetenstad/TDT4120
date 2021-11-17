
def knapsack(n, W, w, v):
    """
    KNAPSACK

    Time Complexity: Theta(nW) = Theta(n2^m)
    """
    if n == 0:
        return 0
    x = knapsack(n - 1, W)
    if w[n] > W:
        return x
    else:
        y = knapsack(n - 1, W - w[n]) + v[n]
        return max(x, y)


def bottom_up_knapsack(n, W, w, v):
    """
    KNAPSACK'

    Time Complexity: Theta(nW) = Theta(n2^m)
    """
    K = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(W + 1):
            x = K[i - 1][j]
            if j < w[i]:
                K[i][j] = x
            else:
                y = K[i - 1][j - w[i]] + v[i]
                K[i][j] = max(x, y)


def continous_knapsack():
    pass # TODO: implement continous knapsack
