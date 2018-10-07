'''
Check whether a binary tree is a full binary tree or not
A full binary tree is defined as a binary tree in which all nodes have either zero or two child nodes. Conversely, there is no node in a full binary tree, which has one child node. More information about full binary trees can be found here.

For Example :
Full

Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.




To check whether a binary tree is a full binary tree we need to test the following cases:-

1) If a binary tree node is NULL then it is a full binary tree.
2) If a binary tree node does have empty left and right sub-trees, then it is a full binary tree by definition.
3) If a binary tree node has left and right sub-trees, then it is a part of a full binary tree by definition. In this case recursively check if the left and right sub-trees are also binary trees themselves.
4) In all other combinations of right and left sub-trees, the binary tree is not a full binary tree.

Following is the implementation for checking if a binary tree is a full binary tree.
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

    def FullBinaryTree(self,start,tmp):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(True)
        elif start.left!=None and start.right!=None:
            tmp.append(True)
        else:
            tmp.append(False)
        self.FullBinaryTree(start.left,tmp)
        self.FullBinaryTree(start.right,tmp)

    def CheckFullBinaryTree(self):

        start=self.root
        tmp=[]
        self.FullBinaryTree(start,tmp)

        flg=True
        for key in tmp:
            if key==False:
                flg=False
                break
        return flg

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.print_tree('preorder'))
    print(tree.CheckFullBinaryTree())

if __name__=='__main__':
    main()