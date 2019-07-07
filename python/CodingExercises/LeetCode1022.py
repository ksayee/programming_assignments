'''
1022. Sum of Root To Leaf Binary Numbers
Easy
Given a binary tree, each node has value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.
Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
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

    def GetRootToLeaf(self,start,tmp,fnl_lst):
        if start.left is None and start.right is None:
            tmp.append(start.value)
            fnl_lst.append(tmp.copy())
            tmp.pop()
            return
        tmp.append(start.value)
        self.GetRootToLeaf(start.left,tmp,fnl_lst)
        self.GetRootToLeaf(start.right,tmp,fnl_lst)
        tmp.pop()

    def PrintSum(self):
        start=self.root
        fnl_lst=[]
        tmp=[]
        self.GetRootToLeaf(start,tmp,fnl_lst)

        sum=0
        for lst in fnl_lst:
            lst.reverse()
            tmp_sum=0
            for i in range(0,len(lst)):
                tmp_sum=tmp_sum+(math.pow(2,i)*lst[i])
            sum=sum+tmp_sum
        return int(sum)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(0)
    tree.root.right=Node(1)
    tree.root.left.left=Node(0)
    tree.root.left.right= Node(1)
    tree.root.right.left = Node(0)
    tree.root.right.right = Node(1)
    print(tree.PrintPreorder())
    print(tree.PrintSum())

if __name__=='__main__':
    main()