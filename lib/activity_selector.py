
def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        return {s[m]}.union(recursive_activity_selector(s, f, m, n))
    else:
        return set()

def greedy_activity_selector(s, f):
    n = s.length
    A = set(s[0])
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.add(s[m])
            k = m
    return A
