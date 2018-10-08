'''
94. Binary Tree Inorder Traversal
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, return the inorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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

    def LeetCode94(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        start=start.left
        tmp=[]
        while start!=None or len(node_lst)!=0:
            while start!=None:
                node_lst.append(start)
                start=start.left
            n=node_lst[-1]
            node_lst.pop()
            tmp.append(str(n.value))
            start=n.right
        return '-'.join(tmp)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left= Node(4)
    tree.root.left.right = Node(5)
    print(tree.PrintTree("Inorder"))
    print(tree.LeetCode94())

if __name__=='__main__':
    main()