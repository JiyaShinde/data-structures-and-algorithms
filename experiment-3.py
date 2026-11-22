class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def Insert(root, value):
    if root is None:
        newNode = Node(value)
        return newNode

    if value < root.data:
        root.left = Insert(root.left, value)

    elif value > root.data:
        root.right = Insert(root.right, value)

    else:
        print("Duplicate Employee ID")

    return root


def CopyTree(root):
    if root is None:
        return None

    newNode = Node(root.data)
    newNode.left = CopyTree(root.left)
    newNode.right = CopyTree(root.right)

    return newNode


def LevelOrder(root):
    if root is None:
        print("Tree is Empty")
        return

    Q = []
    Q.append(root)

    while len(Q) > 0:
        current = Q.pop(0)

        print(current.data, end=" ")

        if current.left is not None:
            Q.append(current.left)

        if current.right is not None:
            Q.append(current.right)


def Height(root):
    if root is None:
        return -1

    leftHeight = Height(root.left)
    rightHeight = Height(root.right)

    return max(leftHeight, rightHeight) + 1


def PrintLeafNodes(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return

    PrintLeafNodes(root.left)
    PrintLeafNodes(root.right)


def Main():
    root = None
    copyRoot = None

    while True:
        print("\n=====================================")
        print("Employee Database Analysis using BST")
        print("=====================================")
        print("1. Insert Employee IDs")
        print("2. Display Original BST (Level Order)")
        print("3. Copy BST")
        print("4. Display Copied BST (Level Order)")
        print("5. Find Height of BST")
        print("6. Display Leaf Nodes")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            n = int(input("Enter number of employee IDs: "))

            for i in range(n):
                value = int(input("Enter Employee ID: "))
                root = Insert(root, value)

        elif choice == 2:
            print("Original BST (Level Order)")
            LevelOrder(root)
            print()

        elif choice == 3:
            copyRoot = CopyTree(root)
            print("BST Copied Successfully")

        elif choice == 4:
            print("Copied BST (Level Order)")
            LevelOrder(copyRoot)
            print()

        elif choice == 5:
            height = Height(root)
            print("Height of BST =", height)

        elif choice == 6:
            print("Leaf Nodes are")
            PrintLeafNodes(root)
            print()

        elif choice == 7:
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice")


Main()
