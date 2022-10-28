class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def enQ(self, data):
        self.item.append(data)

    def deQ(self):
        return self.item.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            cur = self.root
            while True:

                if data < cur.data:
                    if cur.left is None:
                        cur.left = newNode
                        break
                    cur = cur.left
                elif data >= cur.data:
                    if cur.right is None:
                        cur.right = newNode
                        break
                    cur = cur.right    

        return self.root

    def Inorder(self, node):
        if node is None:
            return
        print(node, '', end='')
        self.Inorder(node.left)
        self.Inorder(node.right)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node, '', end='')
        self.inOrder(node.right)

    def Postorder(self, node):
        if node is None:
            return
        self.Postorder(node.left)
        self.Postorder(node.right)
        print(node, '', end='')

    def Breadth(self):
        storeNode = Queue()
        storeNode.enQ(self.root)
        while not storeNode.isEmpty():
            popNode = storeNode.deQ()
            print(popNode, '', end='')
            if popNode.left is not None:
                storeNode.enQ(popNode.left)
            if popNode.right is not None:
                storeNode.enQ(popNode.right)

print(" *** Binary Search Tree ***")
inp = [int(i) for i in input('Enter Input : ').split()]

tree = BST()

for i in inp:
    root = tree.insert(i)
print("\n --- Tree traversal ---")    
print('Level order : ', end='')
tree.Breadth()
print('\nPreorder : ', end='')
tree.Inorder(root)
print('\nInorder : ', end='')
tree.inOrder(root)
print('\nPostorder : ', end='')
tree.Postorder(root)
