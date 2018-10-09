'''
671. Second Minimum Node In a Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
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

    def print_tree(self,traversal_type):
        start=self.root
        tmp=[]
        if traversal_type=='preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)

    def GetNodeValues(self,start,tmp):

        if start is None:
            return
        tmp.append(start.value)
        self.GetNodeValues(start.left,tmp)
        self.GetNodeValues(start.right,tmp)

    def LeetCode671(self):

        start=self.root
        tmp=[]
        self.GetNodeValues(start,tmp)

        sort_lst=sorted(set(tmp))
        if len(sort_lst)>1:
            return sort_lst[1]
        else:
            return -1

def main():

    tree1=BinaryTree(2)
    tree1.root.left=Node(2)
    tree1.root.right=Node(5)
    tree1.root.right.left=Node(5)
    tree1.root.right.right = Node(7)
    print(tree1.print_tree('preorder'))
    print(tree1.LeetCode671())

    tree = BinaryTree(2)
    tree.root.left = Node(2)
    tree.root.right = Node(2)
    print(tree.print_tree('preorder'))
    print(tree.LeetCode671())


if __name__=='__main__':
    main()