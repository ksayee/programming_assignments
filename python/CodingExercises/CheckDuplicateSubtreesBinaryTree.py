'''
Check if a Binary Tree contains duplicate subtrees of size 2 or more
Given a Binary Tree, check whether the Binary tree contains a duplicate sub-tree of size 2 or more.
Note : Two same leaf nodes are not considered as subtree size of a leaf node is one.

Input :  Binary Tree
               A
             /    \
           B        C
         /   \       \
        D     E       B
                     /  \
                    D    E
Output : Yes
Asked in : Google Interview
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
Tree
Tree with duplicate Sub-Tree [ highlight by blue color ellipse ]

[ Method 1]
A simple solution is that, we pick every node of tree and try to find is any sub-tree of given tree is present in tree which is identical with that sub-tree. Here we can use below post to find if a subtree is present anywhere else in tree.
Check if a binary tree is subtree of another binary tree

[Method 2 ]( Efficient solution )
An Efficient solution based on tree serialization and hashing. The idea is to serialize subtrees as strings and store the strings in hash table. Once we find a serialized tree (which is not a leaf) already existing in hash-table, we return true.
Below c++ implementation of above idea.
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

    def CheckDuplicate(self,start,dict,flg_lst):

        if start is None:
            return
        if start.left!=None or start.right!=None:
            tmp=[]
            if start.left!=None:
                tmp.append(start.left.value)
            if start.right!=None:
                tmp.append(start.right.value)
            if start.value in dict.keys():
                val=dict[start.value]
                if sorted(val)==sorted(tmp):
                    flg_lst.append(True)
            else:
                dict[start.value]=tmp
        self.CheckDuplicate(start.left,dict,flg_lst)
        self.CheckDuplicate(start.right,dict,flg_lst)


    def CheckDuplicateSubtreesBinaryTree(self):

        start=self.root
        dict={}
        flg_lst=[]
        self.CheckDuplicate(start,dict,flg_lst)
        if len(flg_lst)>0:
            return True
        else:
            return Falsegit


def main():

    tree=BinaryTree('A')
    tree.root.left=Node('B')
    tree.root.right=Node('C')
    tree.root.left.left=Node('D')
    tree.root.left.right = Node('E')
    tree.root.right.right = Node('B')
    tree.root.right.right.left = Node('D')
    tree.root.right.right.right=Node('E')
    print(tree.print_tree('preorder'))
    print(tree.CheckDuplicateSubtreesBinaryTree())

if __name__=='__main__':
    main()