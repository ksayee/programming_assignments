'''
226. Invert Binary Tree
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
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

        if start is None:
            return
        tmp.append(str(start.value))
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def inorder(self,start,tmp):

        if start is None:
            return
        self.inorder(start.left,tmp)
        tmp.append(str(start.value))
        self.inorder(start.right,tmp)

    def PrintTree(self,traversal):

        start = self.root
        tmp = []
        if traversal=='Preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)
        if traversal=='Inorder':
            self.inorder(start,tmp)
            return '-'.join(tmp)

    def InvertBinaryTree(self,start):

        if start is None:
            return
        self.InvertBinaryTree(start.left)
        self.InvertBinaryTree(start.right)

        tmp=start.left
        start.left=start.right
        start.right=tmp

    def LeetCode226(self):

        start=self.root
        self.InvertBinaryTree(start)
    
def main():

    tree=BinaryTree(4)
    tree.root.left=Node(2)
    tree.root.right = Node(7)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(9)
    print(tree.PrintTree("Preorder"))
    print(tree.LeetCode226())
    print(tree.PrintTree("Preorder"))

    tree1 = BinaryTree(4)
    tree1.root.left = Node(2)
    tree1.root.right = Node(5)
    tree1.root.left.left = Node(1)
    tree1.root.left.right = Node(3)
    print(tree1.PrintTree("Preorder"))
    print(tree1.LeetCode226())
    print(tree1.PrintTree("Preorder"))

if __name__=='__main__':
    main()