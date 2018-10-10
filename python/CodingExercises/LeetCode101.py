'''
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
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

    def inorder(self,start,tmp):

        if start is None:
            return
        self.inorder(start.left,tmp)
        tmp.append(str(start.value))
        self.inorder(start.right,tmp)

    def PrintTree(self,traversal):

        start = self.root
        tmp = []
        if traversal=='Preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)
        if traversal=='Inorder':
            self.inorder(start,tmp)
            return '-'.join(tmp)

    def CheckMirrorImage(self,start1,start2,tmp):

        if start1 is None and start2 is None:
            tmp.append(True)
            return
        if start1!=None  and start2 is None:
            tmp.append(False)
            return
        if start1 is None and start2!=None:
            tmp.append(False)
            return

        if start1.value==start2.value:
            tmp.append(True)
        self.CheckMirrorImage(start1.left,start2.right,tmp)
        self.CheckMirrorImage(start1.right,start2.left,tmp)

    def LeetCode101(self):

        start1=self.root
        start2=self.root

        tmp=[]
        self.CheckMirrorImage(start1,start2,tmp)
        flg=True
        for l in tmp:
            if l==False:
                flg=False
                break
        return flg

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(3)
    print(tree.PrintTree("Preorder"))
    print(tree.LeetCode101())

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(2)
    tree1.root.left.right = Node(3)
    tree1.root.right.right = Node(3)
    print(tree1.PrintTree("Preorder"))
    print(tree1.LeetCode101())

if __name__=='__main__':
    main()