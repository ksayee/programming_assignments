'''
Count subtrees that sum up to a given value x
Given a binary tree containing n nodes. The problem is to count subtress having total node’s data sum equal to a given value x.

Examples:

Input :
             5
           /   \
        -10     3
        /  \   /  \
       9    8 -4   7

       x = 7

Output : 2
There are 2 subtrees with sum 7.

1st one is leaf node:
7.

2nd one is:

      -10
     /   \
    9     8
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

    def print_tree(self,traversal_type):
        start=self.root
        tmp=[]
        if traversal_type=='preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)

    def GetSubTreeSum(self,start,tmp,fnl_lst):

        if start is None:
            return
        if start.left!=None or start.right!=None:
            if start.left!=None and start.right!=None:
                tmp=[]
                tmp.append(start.value)
                tmp.append(start.left.value)
                tmp.append(start.right.value)
            elif start.left!=None and start.right is None:
                tmp=[]
                tmp.append(start.value)
                tmp.append(start.left.value)
            elif start.left is None and start.right!=None:
                tmp=[]
                tmp.append(start.value)
                tmp.append(start.right.value)
            sum=0
            for l in tmp:
                sum=sum+l
            tup=(tmp.copy(),sum)
            fnl_lst.append(tup)
        if start.left is None and start.right is None:
            tmp=[]
            tmp.append(start.value)
            tup=(tmp.copy(),start.value)
            fnl_lst.append(tup)
        self.GetSubTreeSum(start.left,tmp,fnl_lst)
        self.GetSubTreeSum(start.right,tmp,fnl_lst)

    def CountSubTreesSumUpGivenValueBinaryTree(self,k):

        start=self.root
        tmp=[]
        fnl_lst=[]
        self.GetSubTreeSum(start,tmp,fnl_lst)

        out_lst=[]
        for key in fnl_lst:
            if key[1]==k:
                out_lst.append(key[0])

        if len(out_lst)>0:
            return out_lst
        else:
            return -1

def main():

    tree1=BinaryTree(5)
    tree1.root.left=Node(-10)
    tree1.root.right=Node(3)
    tree1.root.left.left=Node(9)
    tree1.root.left.right=Node(8)
    tree1.root.right.left=Node(4)
    tree1.root.right.right = Node(7)
    print(tree1.print_tree('preorder'))
    k=7
    print(tree1.CountSubTreesSumUpGivenValueBinaryTree(k))

if __name__=='__main__':
    main()