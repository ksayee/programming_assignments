'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
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

    def GenerateFunction(self):

        start=self.root


def main():

    tree=BinaryTree('*')
    tree.root.left=Node('+')
    tree.root.right = Node('+')
    tree.root.left.left = Node('3')
    tree.root.left.right = Node('2')
    tree.root.right.left= Node('4')
    tree.root.right.right = Node('5')
    print(tree.print_tree('preorder'))

if __name__=='__main__':
    main()