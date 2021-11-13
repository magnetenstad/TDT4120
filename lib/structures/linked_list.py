
class LinkedListElement:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None


def list_search(L, k):
    x = L.head
    while x != None and x.key != k:
        x = x.next
    return x

def list_insert(L, x):
    x.next = L.head
    if L.head != None:
        L.head.prev = x
    L.head = x
    x.prev = None

def list_delete(L, x):
    if x.prev != None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next != None:
        x.next.prev = x.prev


if __name__ == '__main__':
    L = LinkedList()
    list_insert(L, LinkedListElement(1))
    list_insert(L, LinkedListElement(5))
    list_insert(L, LinkedListElement(7))
    e1 = list_search(L, 1)
    e5 = list_search(L, 5)
    e7 = list_search(L, 7)
    assert e1.key == 1
    assert e5.key == 5
    assert e7.key == 7
    list_delete(L, e1)
    assert list_search(L, 1) == None
