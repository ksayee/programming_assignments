'''
100. Same Tree
Easy
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true
Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
'''

import math

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        if (start.left is None and start.right!=None):
            tmp.append(str(start.value))
            tmp.append(str('NONE'))
        else:
            tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintPreorder(self,start):
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def PrintSameTree(self,start2):
        start1=self.root
        tmp1=self.PrintPreorder(start1)
        tmp2=self.PrintPreorder(start2)
        print(tmp1,tmp2)
        if tmp1==tmp2:
            return True
        else:
            return False

def main():

    tree1=BinaryTree(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)

    tree2 = BinaryTree(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)
    print(tree1.PrintSameTree(tree2.root))

    tree3 = BinaryTree(1)
    tree3.root.left = Node(2)

    tree4 = BinaryTree(1)
    tree4.root.right = Node(2)
    print(tree3.PrintSameTree(tree4.root))

    tree5 = BinaryTree(1)
    tree5.root.left = Node(2)
    tree5.root.right = Node(1)

    tree6 = BinaryTree(1)
    tree6.root.left = Node(1)
    tree6.root.right = Node(2)
    print(tree5.PrintSameTree(tree6.root))

if __name__=='__main__':
    main()