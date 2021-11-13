
class Queue(dict):
    def __init__(self, length) -> None:
        self.length = length
        self.tail = 0
        self.head = 0

def enqueue(Q, x):
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 0
    else:
        Q.tail += 1

def dequeue(Q):
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 0
    else:
        Q.head += 1
    return x

if __name__ == '__main__':
    Q = Queue(5)
    enqueue(Q, 1)
    enqueue(Q, 5)
    enqueue(Q, 7)
    assert dequeue(Q) == 1
    assert dequeue(Q) == 5
    assert dequeue(Q) == 7
