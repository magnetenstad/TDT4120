
# 1) Implementation from Cormen

# class Queue(list):
#     def __init__(self, length) -> None:
#         self.length = length
#         self.extend([None] * length)
#         self.tail = 0
#         self.head = 0

# def enqueue(Q, x):
#     Q[Q.tail] = x
#     if Q.tail == Q.length:
#         Q.tail = 0
#     else:
#         Q.tail += 1

# def dequeue(Q):
#     x = Q[Q.head]
#     if Q.head == Q.length:
#         Q.head = 0
#     else:
#         Q.head += 1
#     return x


# 2) Better implementation in Python

from collections import deque

class Queue(deque):
    pass

def enqueue(Q, x):
    Q.appendleft(x)

def dequeue(Q):
    return Q.pop()


if __name__ == '__main__':
    Q = Queue()
    enqueue(Q, 1)
    enqueue(Q, 5)
    enqueue(Q, 7)
    assert dequeue(Q) == 1
    assert dequeue(Q) == 5
    assert dequeue(Q) == 7
