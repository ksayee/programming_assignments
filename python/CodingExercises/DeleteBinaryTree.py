'''
Write a program to Delete a Tree
To delete a tree we must traverse all the nodes of the tree and delete them one by one.
So which traversal we should use – Inorder or Preorder or Postorder.
Answer is simple – Postorder, because before deleting the parent node we should delete its children nodes first
We can delete tree with other traversals also with extra space complexity
but why should we go for other traversals
if we have Postorder available which does the work without storing anything in same time complexity.
For the following tree nodes are deleted in order – 4, 5, 2, 3, 1
Example Tree
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def RecurrsiveDeleteBinaryTree(self,start):
        if start is None:
            return
        self.RecurrsiveDeleteBinaryTree(start.left)
        self.RecurrsiveDeleteBinaryTree(start.right)
        start.left=None
        start.right=None

    def PreorderTraversal(self,start,tmp):
        if start is None:
            return
        tmp.append(start.data)
        self.PreorderTraversal(start.left,tmp)
        self.PreorderTraversal(start.right,tmp)

    def DeleteBinaryTree(self):
        start=self.root
        tmp=[]
        self.PreorderTraversal(start,tmp)
        print("PreOrder Traversal:",tmp)
        print("Start Deletion")
        start = self.root
        self.RecurrsiveDeleteBinaryTree(start)
        print("Completed Deletion")
        self.root=None
        start = self.root
        tmp = []
        self.PreorderTraversal(start, tmp)
        print("PreOrder Traversal:", tmp)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.DeleteBinaryTree()

if __name__=='__main__':
    main()