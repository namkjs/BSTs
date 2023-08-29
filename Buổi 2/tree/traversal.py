# Function to do postorder traversal of BST
def printPostOrder(root):
    if root!=None:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.key, end=" ")

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.key,end=" ")
        printInorder(root.right)
def printPreOrder(node):
    if node is None:
        return
    print(node.key, end = " ")
    printPreOrder(node.left)
    printPreOrder(node.right)