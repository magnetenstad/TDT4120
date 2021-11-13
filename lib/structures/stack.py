
class Stack(dict):
    def __init__(self):
        super().__init__()
        self.top = 0

def stack_empty(S):
    return S.top == 0

def push(S, x):
    S.top += 1
    S[S.top] = x

def pop(S):
    if stack_empty(S):
        print("ERROR: underflow")
    else:
        S.top -= 1
        return S[S.top + 1]

if __name__ == '__main__':
    S = Stack()
    push(S, 1)
    push(S, 5)
    push(S, 7)
    assert pop(S) == 7
    assert pop(S) == 5
    assert pop(S) == 1