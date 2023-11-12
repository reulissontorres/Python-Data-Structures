from trees.binaryTree import BinnaryTree, Node

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')

a.left = b
b.isLeft = True
b.father = a

a.right = c
c.father = a

b.left = d
d.isLeft = True
d.father = b

bt = BinnaryTree(a)

bt.inOrder(a)
print('\n')
bt.preOrder(a)
print('\n')
bt.postOrder(a)