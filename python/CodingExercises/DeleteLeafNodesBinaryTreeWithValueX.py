'''
Delete leaf nodes with value as x
Given a binary tree and a target integer x,
delete all the leaf nodes having value as x.
Also, delete the newly formed leaves with the target value as x.
Example:
Input : x = 5
            6
         /     \
        5       4
      /   \       \
     1     2       5
Output :
            6
         /     \
        5       4
      /   \
     1     2
Inorder Traversal is 1 5 2 6 4
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def InorderTraversal(self,start,tmp):
        if start is None:
            return
        self.InorderTraversal(start.left,tmp)
        tmp.append(start.data)
        self.InorderTraversal(start.right,tmp)

    def DeleteLeaf(self,start,x):
        if start is None:
            return
        if start.left!=None:
            if (start.left.left is None and start.left.right is None) and start.left.data==x:
                start.left=None
        if start.right!=None:
            if (start.right.left is None and start.right.right is None) and start.right.data==x:
                start.right=None
        self.DeleteLeaf(start.left,x)
        self.DeleteLeaf(start.right,x)

    def DeleteLeafNodesBinaryTreeWithValueX(self,x):
        start=self.root
        tmp=[]
        self.InorderTraversal(start,tmp)
        print("Before Deletion:",tmp)
        start=self.root
        self.DeleteLeaf(start,x)

        start = self.root
        tmp = []
        self.InorderTraversal(start, tmp)
        print("After Deletion:", tmp)



def main():

    tree=BinaryTree(6)
    tree.root.left=Node(5)
    tree.root.right = Node(4)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(2)
    tree.root.right.right = Node(5)
    x=5
    tree.DeleteLeafNodesBinaryTreeWithValueX(x)

if __name__=='__main__':
    main()