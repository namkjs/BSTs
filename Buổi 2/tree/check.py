def maxValue(node):
    if node is None:
        return 0
     
    leftMax = maxValue(node.left)
    rightMax = maxValue(node.right)
     
    value = 0
    if leftMax > rightMax:
        value = leftMax
    else:
        value = rightMax
     
    if value < node.key:
        value = node.key
     
    return value
     
def minValue(node):
    if node is None:
        return 1000000000
     
    leftMax = minValue(node.left)
    rightMax = minValue(node.right)
     
    value = 0
    if leftMax < rightMax:
        value = leftMax
    else:
        value = rightMax
     
    if value > node.key:
        value = node.key
     
    return value
 
# Returns true if a binary tree is a binary search tree
def isBST(node):
    if node is None:
        return True
     
    # false if the max of the left is > than us
    if(node.left is not None and maxValue(node.left) > node.key):
        return False
     
    # false if the min of the right is <= than us
    if(node.right is not None and minValue(node.right) < node.key):
        return False
     
    #false if, recursively, the left or right is not a BST
    if(isBST(node.left) is False or isBST(node.right) is False):
        return False
     
    # passing all that, it's a BST
    return True