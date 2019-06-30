'''
112. Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
        tmp.append(str(start.value))
        self.PreOrder(start.left,tmp)
        self.PreOrder(start.right,tmp)

    def PrintPreOrder(self):
        start=self.root
        tmp=[]
        self.PreOrder(start,tmp)
        return '-'.join(tmp)

    def CheckSum_recur(self,start,tmp,fnl_lst):
        if start is None:
            return
        tmp.append(start.value)
        if start.left is None and start.right is None:
            fnl_lst.append(tmp.copy())
        self.CheckSum_recur(start.left, tmp, fnl_lst)
        self.CheckSum_recur(start.right, tmp, fnl_lst)
        tmp.pop()

    def CheckSum(self,sum):
        start=self.root
        tmp=[]
        fnl_lst=[]
        self.CheckSum_recur(start,tmp,fnl_lst)

        out_lst=[]
        for lst in fnl_lst:
            k=0
            for key in lst:
                k=k+key
            if k==sum:
                out_lst.append(lst.copy())

        return out_lst

def main():

    tree=BinaryTree(5)
    tree.root.left=Node(4)
    tree.root.right = Node(8)
    tree.root.left.left = Node(11)
    tree.root.left.left.left = Node(7)
    tree.root.left.left.right= Node(2)
    tree.root.right.left = Node(13)
    tree.root.right.right = Node(4)
    tree.root.right.right.right = Node(1)
    print(tree.PrintPreOrder())
    sum=22
    print(tree.CheckSum(sum))

if __name__=='__main__':
    main()