class TreeNode(object):

    def __init__(self, x):

        self.val = x

        self.left = None

        self.right = None

def insert(root, newtreein):
    if root is None:
        root = TreeNode(newtreein)
        return root
    if newtreein < root.val:
        root.left= insert(root.left, newtreein)
    else:
        root.right = insert(root.right, newtreein)
    return root


def list_to_bst(listtree):
    if not listtree:
        return None
    pos = (len(listtree)) // 2
    root = TreeNode(listtree[pos])
    root.left = list_to_bst(listtree[:pos])
    root.right = list_to_bst(listtree[pos + 1:])
    return root


def preOrder(node):

    if not node:

        return

    print(node.val)

    preOrder(node.left)

    preOrder(node.right)



def printBST(node,level = 0):

    if node != None:

        printBST(node.right, level + 1)

        print('     ' * level, node.val)

        printBST(node.left, level + 1)



list_nums = sorted([int(item) for item in input("Enter list : ").split()])

result = list_to_bst(list_nums)



print("\nList to a height balanced BST : ")

print(preOrder(result))

print("\nBST model : ")

printBST(result)