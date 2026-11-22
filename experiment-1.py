class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def CreateTree():
    value = int(input("Enter node value (-1 for no node): "))

    if value == -1:
        return None

    newNode = Node(value)

    print("Enter left child of", value)
    newNode.left = CreateTree()

    print("Enter right child of", value)
    newNode.right = CreateTree()

    return newNode


def Inorder(root):
    if root is None:
        return

    Inorder(root.left)
    print(root.data, end=" ")
    Inorder(root.right)


def Preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    Preorder(root.left)
    Preorder(root.right)


def Postorder(root):
    if root is None:
        return

    Postorder(root.left)
    Postorder(root.right)
    print(root.data, end=" ")


def Main():
    root = None

    print("Create Binary Tree")
    root = CreateTree()

    print("\nInorder Traversal")
    Inorder(root)

    print("\nPreorder Traversal")
    Preorder(root)

    print("\nPostorder Traversal")
    Postorder(root)


Main()
