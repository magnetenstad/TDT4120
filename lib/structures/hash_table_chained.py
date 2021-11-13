
class HashTableElement:
    def __init__(self, key) -> None:
        self.key = key

class HashTableChained(list):
    def __init__(self, length) -> None:
        self.extend([[]] * length)


def h(k):
    return k


def chained_hash_insert(T, x):
    T[h(x.key)].append(x)


def chained_hash_search(T, k):
    for x in T[h(k)]:
        if x.key == k:
            return x
    return None


def chained_hash_delete(T, x):
    T[h(x.key)].remove(x)


if __name__ == '__main__':
    T = HashTableChained(100)
    e1 = HashTableElement(1)
    e5 = HashTableElement(5)
    e7 = HashTableElement(7)
    chained_hash_insert(T, e1)
    chained_hash_insert(T, e5)
    chained_hash_insert(T, e7)
    assert chained_hash_search(T, 1) == e1
    assert chained_hash_search(T, 5) == e5
    assert chained_hash_search(T, 7) == e7
    chained_hash_delete(T, e1)
    assert chained_hash_search(T, 1) == None