'''
993. Cousins in Binary Tree
Easy
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:
Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
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
        tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintPreorder(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def CheckCousins(self,n1,n2):

        start=self.root
        nodes=[]
        dict={}
        height=0
        nodes.append(start)
        nodes.append('NONE')
        dict[start.value]=(start.value,height)

        while len(nodes)>0:
            tmp=[]
            while nodes[0]!='NONE':
                n=nodes[0]
                nodes.pop(0)
                if n.left is None and n.right is None:
                    tup=(n.value,'NULL')
                    tmp.append(tup)
                if n.left!=None:
                    tup=(n.value,n.left.value)
                    nodes.append(n.left)
                    tmp.append(tup)
                if n.right!=None:
                    tup=(n.value,n.right.value)
                    nodes.append(n.right)
                    tmp.append(tup)
            height = height + 1
            for tup in tmp:
                if tup[1]!='NULL':
                    dict[tup[1]]=(tup[0],height)
            if nodes[-1]=='NONE' and len(nodes)==1:
                break
            nodes.pop(0)
            nodes.append('NONE')
        print(dict)

        if dict[n1][0]!=dict[n2][0] and dict[n1][1]==dict[n2][1]:
            return True
        else:
            return False

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    print(tree.PrintPreorder())
    print(tree.CheckCousins(4,3))

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.right = Node(4)
    tree1.root.right.right = Node(5)
    print(tree1.PrintPreorder())
    print(tree1.CheckCousins(5, 4))

if __name__=='__main__':
    main()