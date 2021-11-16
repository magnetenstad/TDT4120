
class Table:
    def __init__(self) -> None:
        self.table = []
        self.size = 0
        self.num = 0


def table_insert(T, x):
    if T.size == 0:
        T.table = [None]
        T.size = 1
    if T.num == T.size:
        new_table = [None] * (T.size * 2)
        for i in range(len(T.table)):
            new_table[i] = T.table[i]
        T.table = new_table
        T.size *= 2
    T.table[T.num] = x
    T.num += 1


def table_delete(T, x):
    T.table[T.table.index(x)] = None
    T.num -= 1
    if T.num < T.size//4:
        new_table = [None] * (T.size//2)
        j = 0
        for i in range(len(T.table)):
            if T.table[i] != None:
                new_table[j] = T.table[i]
                j += 1
        T.table = new_table
        T.size //= 2


if __name__ == '__main__':
    T = Table()
    assert len(T.table) == 0
    table_insert(T, 1)
    assert len(T.table) == 1
    table_insert(T, 5)
    assert len(T.table) == 2
    table_insert(T, 7)
    assert len(T.table) == 4
    table_delete(T, 7)
    assert len(T.table) == 4
    table_delete(T, 5)
    assert len(T.table) == 4
    table_delete(T, 1)
    assert len(T.table) == 2
    assert T.size == 2
    assert T.num == 0
    

