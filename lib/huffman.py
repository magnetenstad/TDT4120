
def huffman(C):
    n = len(C)
    Q = C
    for i in range(n - 1):
        z = Node()
        x = extract_min(Q)
        y = extract_min(Q)
        z.freq = x.freq + y.freq
        insert(Q, z)
    return extract_min(Q)

# TODO: implement extract_min, insert, Node
