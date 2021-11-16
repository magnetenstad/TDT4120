
def cut_rod(p, n):
    """
    CUT-ROD

    Time Complexity: O(2^n)
    """
    if n == 0:
        return 0
    q = -float('inf')
    for i in range(1, n + 1):
        q = max(q, p[i - 1] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p, n):
    """
    MEMOIZED-CUT-ROD

    Time Complexity: O(n^2)
    """
    r = [-float('inf')] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n - 1] >= 0:
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n + 1):
            q = max(q, p[i - 1] + memoized_cut_rod_aux(p, n - i))
    r[n] = q
    return q


def bottom_up_cut_rod(p, n):
    """
    BOTTOM-UP-CUT-ROD

    Time Complexity: O(n^2)
    """
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p, n):
    """
    EXTENDED-BOTTOM-UP-CUT-ROD

    Time Complexity: O(n^2)
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -float('inf')
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s

def print_cut_rod_solution(p, n):
    """
    PRINT-CUT-ROD-SOLUTION

    Time Complexity: O(n^2)
    """
    _, s = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n -= s[n]
