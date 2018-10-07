'''
Print all k-sum paths in a binary tree
A binary tree and a number k are given. Print every path in the tree with sum of the nodes in the path as k.
A path can start from any node and end at any node and must be downward only, i.e. they need not be root node and leaf node; and negative numbers can also be there in the tree.

Examples:

Input : k = 5
        Root of below binary tree:
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5
        /   / \     \
       1   1   2     6

Output :
3 2
3 1 1
1 3 1
4 1
1 -1 4 1
-1 4 2
5
1 -1 5
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

    def PrintPath(self,tmp,k):

        start=0
        end=len(tmp)-1
        while start<=end:
            p=start
            sum=k
            while sum>0:
                sum=sum-tmp[p]
                if sum==0:
                    print(tmp[start:p+1])
                    break
                if p < len(tmp) - 1:
                    p = p + 1
                else:
                    break
            start=start+1

    def GetKSumPaths(self,start,tmp,k):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
            self.PrintPath(tmp,k)
            tmp.pop()
            return
        tmp.append(start.value)
        self.GetKSumPaths(start.left,tmp,k)
        self.GetKSumPaths(start.right,tmp,k)
        tmp.pop()

    def KSumPathsBinaryTree(self,k):

        start=self.root
        tmp=[]
        self.GetKSumPaths(start,tmp,k)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(3)
    tree.root.right=Node(-1)
    tree.root.left.left=Node(2)
    tree.root.left.right = Node(1)
    tree.root.left.right.left = Node(1)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.left.left = Node(1)
    tree.root.right.left.right = Node(2)
    tree.root.right.right.right = Node(6)
    print(tree.print_tree('preorder'))
    k=5
    tree.KSumPathsBinaryTree(k)

if __name__=='__main__':
    main()