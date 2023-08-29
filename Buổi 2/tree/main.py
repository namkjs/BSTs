from traversal import *
from search import *
from delete import *
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
  
# Function to insert a new node with given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
  
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
  
    # Return the node pointer
    return node
  

def main():
    i = int(0)
    while (i != 6):
        print("Nhập 1 để tạo mới BST\nNhập 2 để thêm node\nNhập 3 để tìm kiếm node\nNhập 4 để xoá node\nNhập 5 để duyệt node\nNhập 6 để thoát")
        i = int(input("Lựa chọn: "))
        if (i == 1):
            root = None
            key = int(input("Nhập giá trị của đỉnh: "))
            root = insert(root, key)
        elif (i == 2):
            a = None
            while(a!=0):
                print("Nhập 0 để dừng thêm node")
                a = int(input("Nhập giá trị của node: "))
                if (a != 0):
                    insert(root, a)
                else:
                    break

        elif (i == 3):
            key = int(input("Nhập giá trị muốn tìm kiếm: "))
            if search(root, key) is None:
                print(f"{key} không xuất hiện trong cây")
            else:
                print(f"{key} xuất hiện trong cây")
        elif (i == 4):
            key = int(input("Nhập giá trị cần xoá: "))
            if search(root, key) is None:
                print(f"{key} không xuất hiện trong cây")
            else:
                deleteNode(root, key)
                printInorder(root)
                print("\n")
        elif (i == 5):
            a = 0
            print("Nhập 1 để duyệt cây theo in-order\nNhập 2 để duyệt cây theo pre-order\nNhập 3 để duyệt cây theo post-order\nNhập 4 để quay lại")
            a = int(input(""))
            while(a!=4):
                if (a==1):
                    printInorder(root)
                    print("\n")
                    break
                elif (a==2):
                    printPreOrder(root)
                    print("\n")
                    break
                elif (a==3):
                    printPostOrder(root)
                    print("\n")
                    break
                elif (a==4):
                    break
        elif (i==6):
            break
        else:
            print("Lỗi vui lòng nhập lại: ")


if __name__ == '__main__':
    main()