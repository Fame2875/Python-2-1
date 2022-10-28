class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def insert(self, root, key):

        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, a):

        b = a.right
        T2 = b.left

        b.left = a
        a.right = T2

        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))
        b.height = 1 + max(self.getHeight(b.left),
                           self.getHeight(b.right))

        return b

    def rightRotate(self, b):

        a = b.left
        T3 = a.right

        a.right = b
        b.left = T3

        b.height = 1 + max(self.getHeight(b.left),
                           self.getHeight(b.right))
        a.height = 1 + max(self.getHeight(a.left),
                           self.getHeight(a.right))

        return a

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def print_inorder(self, root):

        if not root:
            return

        self.print_inorder(root.left)
        print("{0} ".format(root.val), end="")
        self.print_inorder(root.right)

    def print_preorder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.print_preorder(root.left)
        self.print_preorder(root.right)

    def print_postorder(self, root):

        if not root:
            return

        self.print_postorder(root.left)
        self.print_postorder(root.right)
        print("{0} ".format(root.val), end="")


print(" *** AVL Tree ***")

input_string = input("Enter some numbers : ")

bst = AVLTree()
root = None
for n in input_string.split():
    root = bst.insert(root, int(n))

print("in_order  --> ", end="")
bst.print_inorder(root)
print()


print("preorder  --> ", end="")
bst.print_preorder(root)
print()

print("postorder --> ", end="")
bst.print_postorder(root)
print()
