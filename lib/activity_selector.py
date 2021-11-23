
def recursive_activity_selector(s, f, k, n):
    """
    RECURSIVE-ACTIVITY-SELECTOR

    Input:
    @param s: start times
    f: finish times
    k: 0
    n: len(s)
    note: A fictitious activity a0 with f0 = 0 must be added to s and f.
    Input must be sorted by finish times.
    """
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return {m}.union(recursive_activity_selector(s, f, m, n)) # a[m]
    else:
        return set()

def greedy_activity_selector(s, f):
    n = len(s)
    A = set(s[0])
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.add(m) # a[m]
            k = m
    return A

if __name__ == '__main__':
    from tests import test_algorithm, get_activity_selector_problem_instances
    test_algorithm(recursive_activity_selector, \
        get_activity_selector_problem_instances())
    