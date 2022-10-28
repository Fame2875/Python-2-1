class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self,k):
        self.root = None
        self.count = 0
        self.k = k


    def insert(self, data):
        if data <= self.k:
                        self.count+=1
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

if __name__ == '__main__':
    inp = input('Enter Input : ').split('/')
    lst = list(map(int, inp[0].split()))
    k = int(inp[1])
    T = BST(k)
    # print(lst, k)
    root = None
    for item in lst:
        root = T.insert(item)
    T.print_tree(root)
    print('--------------------------------------------------')
    print(T.count)