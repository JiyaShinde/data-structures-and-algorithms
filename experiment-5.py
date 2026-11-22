class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    break
                temp = temp.right

    def inorder(self):
        s = Stack()
        temp = self.root

        print("Inorder Traversal:", end=" ")

        while temp is not None or not s.is_empty():
            while temp is not None:
                s.push(temp)
                temp = temp.left

            temp = s.pop()
            print(temp.data, end=" ")
            temp = temp.right

        print()

    def preorder(self):
        if self.root is None:
            return

        s = Stack()
        s.push(self.root)

        print("Preorder Traversal:", end=" ")

        while not s.is_empty():
            temp = s.pop()
            print(temp.data, end=" ")

            if temp.right is not None:
                s.push(temp.right)

            if temp.left is not None:
                s.push(temp.left)

        print()


tree = BST()

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    tree.insert(data)

tree.inorder()
tree.preorder()
