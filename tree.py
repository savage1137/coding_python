class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)

    if val < root.data:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


root = None
values = [10, 5, 15, 3, 7, 12, 18]

for v in values:
    root = insert(root, v)

print("Tree (inorder):")
inorder(root)



