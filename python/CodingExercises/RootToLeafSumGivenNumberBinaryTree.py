'''
Root to leaf path sum equal to a given number
Given a binary tree and a number, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals the given number. Return false if no such path can be found.



For example, in the above tree root to leaf paths exist with following sums.

21 –> 10 – 8 – 3
23 –> 10 – 8 – 5
14 –> 10 – 2 – 2
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

    def RootToLeafSum(self,start,tmp,k,out_lst):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
            sum=0
            for l in tmp:
                sum=sum+l
            if sum==k:
                out_lst.append(True)
            else:
                out_lst.append(False)
            return
        tmp.append(start.value)
        self.RootToLeafSum(start.left, tmp, k, out_lst)
        tmp.pop()
        self.RootToLeafSum(start.right,tmp,k,out_lst)
        tmp.pop()

    def RootToLeafSumGivenNumberBinaryTree(self,k):

        start=self.root
        tmp=[]
        out_lst=[]
        self.RootToLeafSum(start,tmp,k,out_lst)
        flg=False
        for l in out_lst:
            if l==True:
                flg=True
                break
        return flg

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(8)
    tree.root.right=Node(2)
    tree.root.left.left=Node(3)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(2)
    print(tree.print_tree('preorder'))
    k=21
    print(tree.RootToLeafSumGivenNumberBinaryTree(k))
    k = 23
    print(tree.RootToLeafSumGivenNumberBinaryTree(k))
    k = 14
    print(tree.RootToLeafSumGivenNumberBinaryTree(k))
    k = 15
    print(tree.RootToLeafSumGivenNumberBinaryTree(k))

if __name__=='__main__':
    main()