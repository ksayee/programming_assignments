'''
144. Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
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
        tmp.append(start.value)
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)


    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            tmp=[]
            start=self.root
            self.preorder(start,tmp)
            return tmp


    def LeetCode144(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        tmp=[]

        while len(node_lst)!=0:
            n=node_lst[-1]
            tmp.append(n.value)
            node_lst.pop()
            if n.right!=None:
                node_lst.append(n.right)
            if n.left!=None:
                node_lst.append(n.left)
        return tmp


def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    print(tree.print_tree('preorder'))
    print(tree.LeetCode144())

    tree1 = BinaryTree(4)
    tree1.root.left = Node(9)
    tree1.root.right = Node(0)
    tree1.root.left.left=Node(5)
    tree1.root.left.right=Node(1)
    print(tree1.print_tree('preorder'))
    print(tree1.LeetCode144())

if __name__=='__main__':
    main()