
class HashTableOpenAddressing(list):
    def __init__(self, m, length) -> None:
        self.m = m
        self.extend([None] * m * length)


def h(k, i):
    return k * 5 + i


def hash_insert(T, k):
    i = 0

    j = h(k, i)
    if T[j] == None:
        T[j] = k
        return j
    i += 1

    while i != T.m:
        j = h(k, i)
        if T[j] == None:
            T[j] = k
            return j
        i += 1


def hash_search(T, k):
    i = 0

    j = h(k, i)
    if T[j] == k:
        return j
    i += 1

    while T[j] != None and i != T.m:
        j = h(k, i)
        if T[j] == k:
            return j
        i += 1

    return None


if __name__ == '__main__':
    T = HashTableOpenAddressing(2, 100)
    hash_insert(T, 5)
    hash_insert(T, 10)
    assert T[hash_search(T, 5)] == 5
    assert T[hash_search(T, 10)] == 10
    