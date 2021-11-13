
class BinaryTreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None


def inorder_tree_walk(x):
    if x != None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)


def tree_search(x, k):
    if x == None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)

def iterative_tree_search(x, k):
    while x != None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x):
    while x.left != None:
        x = x.left
    return x

def tree_maximum(x):
    while x.right != None:
        x = x.right
    return x


def tree_successor(x):
    if x.right != None:
        return tree_minimum(x.right)
    y = x.p
    while y != None and x == y.right:
        x = y
        y = y.p
    return y


def tree_insert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p


def tree_delete(T, z):
    if z.left == None:
        transplant(T, z, z.right)
    elif z.right == None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


if __name__ == '__main__':
    T = BinaryTree()
    n1 = BinaryTreeNode(1)
    n5 = BinaryTreeNode(5)
    n7 = BinaryTreeNode(7)
    tree_insert(T, n1)
    tree_insert(T, n5)
    tree_insert(T, n7)
    inorder_tree_walk(T.root)
    assert tree_successor(n1) == n5
    assert tree_successor(n5) == n7
    assert tree_successor(n7) == None
    tree_delete(T, n5)
    assert tree_successor(n1) == n7

