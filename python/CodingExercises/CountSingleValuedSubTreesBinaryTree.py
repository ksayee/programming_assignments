'''
Find Count of Single Valued Subtrees
Given a binary tree, write a program to count the number of Single Valued Subtrees. A Single Valued Subtree is one in which all the nodes have same value. Expected time complexity is O(n).

Example:

Input: root of below tree
              5
             / \
            1   5
           / \   \
          5   5   5
Output: 4
There are 4 subtrees with single values.


Input: root of below tree
              5
             / \
            4   5
           / \   \
          4   4   5
Output: 5
There are five subtrees with single values.
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

    def SingleValueSubTree(self,start,tmp):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(1)
            return
        if start.left!=None or start.right!=None:
            if start.left!=None and start.right!=None:
                if start.value==start.left.value and start.value==start.right.value:
                    tmp.append(1)
            elif start.left is None and start.right!=None:
                if start.value==start.right.value:
                    tmp.append(1)
            elif start.left!=None and start.right is None:
                if start.value==start.left.value:
                    tmp.append(1)
        self.SingleValueSubTree(start.left,tmp)
        self.SingleValueSubTree(start.right,tmp)

    def CountSingleValueSubTreesBinaryTree(self):

        start=self.root
        tmp=[]
        self.SingleValueSubTree(start,tmp)
        sum=0
        for l in tmp:
            sum=sum+l
        return sum

    def CountSingleValueSubTreesIterativeBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        tmp=[]

        while len(node_lst)!=0:

            n=node_lst[-1]
            node_lst.pop()

            if n.left is None and n.right is None:
                tmp.append(1)
            elif n.left!=None and n.right!=None:
                if n.value==n.left.value and n.value==n.right.value:
                    tmp.append(1)
            elif n.left!=None and n.right is None:
                if n.value==n.left.value:
                    tmp.append(1)
            elif n.left is None and n.right!=None:
                if n.value==n.right.value:
                    tmp.append(1)
            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)
        sum=0
        for l in tmp:
            sum=sum+l
        return sum

def main():

    tree=BinaryTree(5)
    tree.root.left=Node(1)
    tree.root.right=Node(5)
    tree.root.left.left=Node(5)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(5)
    print(tree.print_tree('preorder'))
    print(tree.CountSingleValueSubTreesBinaryTree())
    print(tree.CountSingleValueSubTreesIterativeBinaryTree())

    tree1 = BinaryTree(5)
    tree1.root.left = Node(4)
    tree1.root.right = Node(5)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(4)
    tree1.root.right.right = Node(5)
    print(tree1.print_tree('preorder'))
    print(tree1.CountSingleValueSubTreesBinaryTree())
    print(tree1.CountSingleValueSubTreesIterativeBinaryTree())

    tree2 = BinaryTree(5)
    tree2.root.left = Node(5)
    tree2.root.right = Node(5)
    tree2.root.left.left = Node(5)
    tree2.root.left.right = Node(5)
    tree2.root.right.right = Node(5)
    print(tree2.print_tree('preorder'))
    print(tree2.CountSingleValueSubTreesBinaryTree())
    print(tree2.CountSingleValueSubTreesIterativeBinaryTree())

    tree3 = BinaryTree('a')
    tree3.root.left = Node('a')
    tree3.root.right = Node('a')
    tree3.root.right.left = Node('a')
    tree3.root.right.right = Node('a')
    tree3.root.right.right.right = Node('A')
    print(tree3.print_tree('preorder'))
    print(tree3.CountSingleValueSubTreesBinaryTree())
    print(tree3.CountSingleValueSubTreesIterativeBinaryTree())

    tree3 = BinaryTree('a')
    tree3.root.left = Node('c')
    tree3.root.right = Node('b')
    tree3.root.right.left = Node('b')
    tree3.root.right.right = Node('b')
    tree3.root.right.right.right = Node('b')
    print(tree3.print_tree('preorder'))
    print(tree3.CountSingleValueSubTreesBinaryTree())
    print(tree3.CountSingleValueSubTreesIterativeBinaryTree())

if __name__=='__main__':
    main()