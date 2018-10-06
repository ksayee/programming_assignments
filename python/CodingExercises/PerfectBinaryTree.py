'''
Check whether a given binary tree is perfect or not
Given a Binary Tree, write a function to check whether the given Binary Tree is a prefect Binary Tree or not.

A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.

Examples:
The following tree is a perfect binary tree

               10
           /       \
         20         30
        /  \        /  \
      40    50    60   70


               18
           /       \
         15         30
The following tree is not a perfect binary tree

      1
    /    \
   2       3
    \     /  \
     4   5    6
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

    def CheckPerfectBinaryTree(self,start,tmp):
        if start is None:
            return
        if start.left is None and start.right is None:
            print("Leaf Node")
        elif start.left is None and start.right!=None:
            tmp.append(False)
        elif start.left!=None and start.right is None:
            tmp.append(False)
        elif start.left!=None and start.right!=None:
            tmp.append(True)
        self.CheckPerfectBinaryTree(start.left,tmp)
        self.CheckPerfectBinaryTree(start.right,tmp)

    def PerfectBinaryTree(self):

        start=self.root
        tmp=[]
        self.CheckPerfectBinaryTree(start,tmp)

        flg=True
        for l in tmp:
            if l==False:
                flg=False
                break
        return flg

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(20)
    tree.root.right=Node(30)
    tree.root.left.left=Node(40)
    tree.root.left.right = Node(50)
    tree.root.right.left = Node(60)
    tree.root.right.right = Node(70)
    print(tree.print_tree('preorder'))
    print(tree.PerfectBinaryTree())

if __name__=='__main__':
    main()