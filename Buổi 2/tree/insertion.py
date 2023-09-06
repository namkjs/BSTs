class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    return node