def search(root, key):
	if root is None or root.key == key:
		return root
	elif root.key < key:
		return search(root.right, key)
	return search(root.left, key)