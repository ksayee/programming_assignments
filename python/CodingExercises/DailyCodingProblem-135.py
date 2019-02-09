'''
This question was asked by Apple.
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrder(self,start,tmp):
        if start is None:
            return
        tmp.append(start.value)
        self.PreOrder(start.left,tmp)
        self.PreOrder(start.right,tmp)

    def PrintTree(self,traversal_type):
        start=self.root
        tmp=[]
        if traversal_type=='PreOrder':
            self.PreOrder(start,tmp)
        return tmp

    def GetMinimumPath(self,start,tmp,fnl_lst,k):
        if start is None:
            return
        tmp.append(start.value)
        if len(tmp)>0:
            sum=0
            for l in tmp:
                sum=sum+l
            if sum==k:
                if tmp not in fnl_lst:
                    fnl_lst.append(tmp.copy())

        self.GetMinimumPath(start.left,tmp,fnl_lst,k)
        self.GetMinimumPath(start.right,tmp,fnl_lst,k)
        tmp.pop()

    def MinimumPath(self,k):
        start=self.root
        tmp=[]
        fnl_lst=[]
        self.GetMinimumPath(start,tmp,fnl_lst,k)
        return fnl_lst

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(5)
    tree.root.right=Node(5)
    tree.root.left.right=Node(2)
    tree.root.right.right=Node(1)
    tree.root.right.right.left=Node(-1)
    print(tree.PrintTree('PreOrder'))
    k=15
    print(tree.MinimumPath(k))

if __name__=='__main__':
    main()