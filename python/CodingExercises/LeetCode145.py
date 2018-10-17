'''
145. Binary Tree PostOrder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def postorder(self,start,tmp):
        if start is None:
            return
        self.postorder(start.left,tmp)
        self.postorder(start.right,tmp)
        tmp.append(start.value)


    def print_tree(self,traversal_type):
        if traversal_type=='postorder':
            tmp=[]
            start=self.root
            self.postorder(start,tmp)
            return tmp


    def LeetCode145(self):

        start=self.root
        stk1=[]
        stk2=[]
        stk1.append(start)

        while len(stk1)!=0:
            n=stk1[-1]
            stk1.pop()
            if n.left!=None:
                stk1.append(n.left)
            if n.right!=None:
                stk1.append(n.right)
            stk2.append(n)

        tmp=[]
        while len(stk2)!=0:
            n=stk2[-1]
            tmp.append(n.value)
            stk2.pop()
        return tmp


def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    print(tree.print_tree('postorder'))
    print(tree.LeetCode145())

    tree1 = BinaryTree(4)
    tree1.root.left = Node(9)
    tree1.root.right = Node(0)
    tree1.root.left.left=Node(5)
    tree1.root.left.right=Node(1)
    print(tree1.print_tree('postorder'))
    print(tree1.LeetCode145())

if __name__=='__main__':
    main()