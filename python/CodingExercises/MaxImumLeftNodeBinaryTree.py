'''
Get maximum left node in binary tree
Given a tree, the task is to find the maximum in an only left node of the binary tree.

Examples:

Input :
           7
         /    \
        6       5
       / \     / \
      4  3     2  1
Output :
6

Input :
            1
         /    \
        2       3
       /       / \
      4       5   6
        \    /  \
         7  8   9
Output :
8
'''

class Node(object):

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):

    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,tmp):
        if start==None:
            return
        tmp.append(str(start.value))
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def print_tree(self,traversal):
        if traversal=='preorder':
            start=self.root
            tmp=[]
            self.preorder(start,tmp)
        return '-'.join(tmp)

    def GetLeftNode(self,start,tmp):

        if start is None:
            return
        if start.left!=None:
            tmp.append(start.left.value)
        self.GetLeftNode(start.left,tmp)
        self.GetLeftNode(start.right,tmp)

    def MaximumLeftNodeBinaryTree(self):

        start=self.root
        tmp=[]
        self.GetLeftNode(start,tmp)

        return sorted(tmp,reverse=True)[0]

def main():

    tree=BinaryTree(7)
    tree.root.left=Node(6)
    tree.root.right=Node(5)
    tree.root.left.left=Node(4)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(1)
    print(tree.print_tree('preorder'))
    print(tree.MaximumLeftNodeBinaryTree())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.left.right = Node(7)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.left.left = Node(8)
    tree.root.right.left.right = Node(9)
    print(tree.print_tree('preorder'))
    print(tree.MaximumLeftNodeBinaryTree())

if __name__=='__main__':
    main()