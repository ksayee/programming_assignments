'''
Subtree with given sum in a Binary Tree
You are given a binary tree and a given sum. The task is to check if there exist a subtree whose sum of all nodes is equal to the given sum.


Examples :

// For above tree
Input : sum = 17
Output: "Yes"
// sum of all nodes of subtree {3, 5, 9} = 17

Input : sum = 11
Output: "No"
// no subtree with given sum exist
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

    def SubTreeGivenSumBinaryTree(self,k):

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

    tree1=BinaryTree(1)
    tree1.root.left=Node(3)
    tree1.root.right=Node(6)
    tree1.root.left.left=Node(5)
    tree1.root.left.right=Node(9)
    tree1.root.right.left=Node(8)
    print(tree1.print_tree('preorder'))
    k=17
    print(tree1.SubTreeGivenSumBinaryTree(k))

if __name__=='__main__':
    main()