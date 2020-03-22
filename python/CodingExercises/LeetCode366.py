'''
Leetcode 366. Find Leaves of Binary Tree
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
Example:
Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5
Output: [[4,5,3],[2],[1]]
'''

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

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def RemoveLeaves(self,start,tmp):
        if start.left is None and start.right is None:
            tmp.append(start.value)
            return True
        if start.left!=None:
            flg=self.RemoveLeaves(start.left,tmp)
            if flg==True:
                start.left=None
        if start.right!=None:
            flg=self.RemoveLeaves(start.right,tmp)
            if flg==True:
                start.right=None
        return False

    def FindLeaves(self):
        start=self.root
        output_lst=[]
        while start!=None:
            tmp=[]
            flg=self.RemoveLeaves(start,tmp)
            output_lst.append(tmp.copy())
            if flg==True:
                start=None
        return output_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.PrintTree())
    print(tree.FindLeaves())
    
if __name__=='__main__':
    main()