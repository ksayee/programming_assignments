'''
437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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

    def GetSumPath(self,start,tmp,fnl_lst,k):

        if start is None:
            return
        tmp.append(start.value)
        sum=0
        for l in tmp:
            sum=sum+l
        if sum==k:
            fnl_lst.append(tmp.copy())
            tmp.pop()
            return
        elif sum>k:
            tmp.pop()
        self.GetSumPath(start.left,tmp,fnl_lst,k)
        self.GetSumPath(start.right,tmp,fnl_lst,k)
        if len(tmp)>0:
            tmp.pop()

    def LeetCode437(self,k):

        start=self.root
        tmp=[]
        fnl_lst=[]
        self.GetSumPath(start,tmp,fnl_lst,k)
        return fnl_lst

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(5)
    tree.root.right=Node(-3)
    tree.root.left.left=Node(3)
    tree.root.left.right = Node(2)
    tree.root.left.left.left = Node(3)
    tree.root.left.left.right = Node(-2)
    tree.root.left.right.right = Node(1)
    tree.root.right.right = Node(11)
    print(tree.print_tree('preorder'))
    k=8
    print(tree.LeetCode437(k))

if __name__=='__main__':
    main()