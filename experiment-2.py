class Node:
    def __init__(self, rollNo):
        self.rollNo = rollNo
        self.left = None
        self.right = None


def Insert(root, rollNo):
    if root is None:
        newNode = Node(rollNo)
        return newNode

    if rollNo < root.rollNo:
        root.left = Insert(root.left, rollNo)

    elif rollNo > root.rollNo:
        root.right = Insert(root.right, rollNo)

    else:
        print("Duplicate Roll Number. Record not inserted.")

    return root


def CreateBST():
    root = None

    n = int(input("Enter number of student records: "))

    for i in range(n):
        rollNo = int(input("Enter roll number: "))
        root = Insert(root, rollNo)

    return root


def InorderNonRecursive(root):
    S = []
    current = root

    while current is not None or len(S) > 0:

        while current is not None:
            S.append(current)
            current = current.left

        current = S.pop()
        print(current.rollNo, end=" ")

        current = current.right


def PreorderNonRecursive(root):
    if root is None:
        return

    S = []
    S.append(root)

    while len(S) > 0:
        current = S.pop()

        print(current.rollNo, end=" ")

        if current.right is not None:
            S.append(current.right)

        if current.left is not None:
            S.append(current.left)


def Main():
    root = CreateBST()

    print("\nStudent Records (Ascending Roll Numbers)")
    InorderNonRecursive(root)

    print("\nStudent Records (Preorder Traversal)")
    PreorderNonRecursive(root)


Main()
