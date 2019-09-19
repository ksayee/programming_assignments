'''
Check if a binary Tree is height balanced.
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def CheckIfBalanced(self,start):
        if start is None:
            return 0
        leftHeight=self.CheckIfBalanced(start.left)
        print(start)
        if leftHeight==-1:
            return -1
        rightHeight=self.CheckIfBalanced(start.right)
        if rightHeight==-1:
            return -1
        if abs(leftHeight-rightHeight)>1:
            return -1
        return 1+max(leftHeight,rightHeight)

    def HeightBalancedBinaryTree(self):
        start=self.root
        value=self.CheckIfBalanced(start)
        if value==-1:
            return False
        else:
            return True

def main():

    tree=BinaryTree(3)
    tree.root.left=Node(1)
    tree.root.right = Node(5)
    tree.root.left.left = Node(0)
    tree.root.left.right = Node(2)
    tree.root.right.left = Node(4)
    tree.root.right.left.right = Node(6)
    print(tree.HeightBalancedBinaryTree())

if __name__=='__main__':
    main()