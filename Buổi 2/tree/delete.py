def deleteNode(root, k):
    if root is None:
        return root

    if root.key > k:
        root.left = deleteNode(root.left, k)
        return root
    elif root.key < k:
        root.right = deleteNode(root.right, k)
        return root
 
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp
 
    else:
 
        succParent = root
        succ = root.right
        while succ.left is not None:
            succParent = succ
            succ = succ.left
 
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.right
        root.key = succ.key
 
        del succ
        return root
 