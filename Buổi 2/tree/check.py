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
 
def isBST(node):
    if node is None:
        return True
    if(node.left is not None and maxValue(node.left) > node.key):
        return False
    if(node.right is not None and minValue(node.right) < node.key):
        return False
    if(isBST(node.left) is False or isBST(node.right) is False):
        return False
    return True