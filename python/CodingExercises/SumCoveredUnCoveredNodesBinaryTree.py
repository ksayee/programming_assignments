'''
Check sum of Covered and Uncovered nodes of Binary Tree
Given a binary tree, you need to check whether sum of all covered elements is equal to sum of all uncovered elements or not.
In a binary tree, a node is called Uncovered if it appears either on left boundary or right boundary. Rest of the nodes are called covered.

For example, consider below binary tree

tree
In above binary tree,
Covered node:     6, 5, 7
Uncovered node:   9, 4, 3, 17, 22, 20

The output for this tree should be false as
sum of covered and uncovered node is not same
return the difference between Uncoverted and Coverved nodes.
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

    def UnCoverLeftSum(self,start,left_lst):

        if start.left is None and start.right is None:
            left_lst.append(start.value)
            return
        if start.left!=None:
            left_lst.append(start.value)
            self.UnCoverLeftSum(start.left,left_lst)
        else:
            left_lst.append(start.value)
            self.UnCoverLeftSum(start.right,left_lst)

    def UnCoverRightSum(self,start,right_lst):

        if start.left is None and start.right is None:
            right_lst.append(start.value)
            return
        if start.right!=None:
            right_lst.append(start.value)
            self.UnCoverLeftSum(start.right,right_lst)
        else:
            right_lst.append(start.value)
            self.UnCoverLeftSum(start.left,right_lst)

    def CompleteSum(self,start,lst):

        if start is None:
            return
        lst.append(start.value)
        self.CompleteSum(start.left,lst)
        self.CompleteSum(start.right,lst)

    def UnCoverSum(self):

        left_sum=0
        left_lst=[]
        right_lst=[]
        lst=[]
        start=self.root
        self.UnCoverLeftSum(start,left_lst)
        self.UnCoverRightSum(start, right_lst)
        self.CompleteSum(start,lst)

        sum=0
        lsum=0
        rsum=0

        for l in lst:
            sum=sum+l
        for l in left_lst:
            lsum=lsum+l
        for l in right_lst:
            rsum=rsum+l

        return sum-(lsum+rsum-start.value)

def main():

    tree=BinaryTree(9)
    tree.root.left=Node(4)
    tree.root.right=Node(17)
    tree.root.left.left=Node(3)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(7)
    tree.root.right.right=Node(22)
    tree.root.right.right.left = Node(20)
    print(tree.print_tree('preorder'))
    print(tree.UnCoverSum())

if __name__=='__main__':
    main()