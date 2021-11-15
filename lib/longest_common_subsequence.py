
def lcs_length(X, Y):
    """
    LCS-LENGTH

    Time Complexity: Theta(m*n)
    Space Complexity: Theta(m*n)
    """
    m = len(X)
    n = len(Y)
    b = [[0] * n for _ in range(m)]
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i - 1][j - 1] = '↖'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i - 1][j - 1] = '↑'
            else:
                c[i][j] = c[i][j - 1]
                b[i - 1][j - 1] = '←'
    return c, b


def print_lcs(b, X, i, j):
    """
    PRINT-LCS

    Time Complexity: Theta(m + n)
    Space Complexity: Theta(1)
    """
    if i == -1 or j == -1:
        return
    if b[i][j] == '↖':
        print_lcs(b, X, i - 1, j - 1)
        print(X[i], end=" ")
    elif b[i][j] == '↑':
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

