class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.father = None
        self.isLeft = False

    def setLeft(self, data):
        self.left = Node(data)
        self.isLeft = True

    def setRight(self, data):
        self.right = Node(data)
        self.isLeft = False


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self, root):
        if root is None:
            return
        print(root.data, sep='-->', end='-->')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, sep='-->', end='-->')
        self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, sep='-->', end='-->')


    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def sumNodes(self, root):
        if root is None:
            return 0
        return root.data + self.sumNodes(root.left) + self.sumNodes(root.right)
 
    def depth(self, root):
        if root is None:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        return 1 + max(left_depth, right_depth)



# Create nodes
root = Node(1)
root.setLeft(2)
root.setRight(3)
root.left.setLeft(4)
root.left.setRight(5)
root.right.setLeft(6)
root.right.setRight(7)

# Create a binary tree with the root node
binary_tree = BinaryTree(root)

# Perform different traversals
print("Pre-order traversal:")
binary_tree.preOrder(root)
print("\n")

print(binary_tree.countNodes(root))
print(binary_tree.sumNodes(root))
print(binary_tree.depth(root))