#
# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        
def binaryTreeInOrderTraversal(root):
    if root:
        binaryTreeInOrderTraversal(root.left)
        print(root.data)
        binaryTreeInOrderTraversal(root.right)    



root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)