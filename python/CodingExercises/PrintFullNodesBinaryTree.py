'''
Print all full nodes in a Binary Tree
Given a binary tree, print all nodes will are full nodes. Full Nodes are nodes which has both left and right children as non-empty.

Examples:

Input :    10
          /  \
         8    2
        / \   /
       3   5 7
Output : 10 8

Input :   1
         / \
        2   3
           / \
          4   6
Output : 1 3
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,traversal):
        if start!=None:
            traversal=traversal+ (str(start.value)+ '-')
            traversal=self.preorder(start.left,traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(self.root,'')
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def GetFullNodes(self,start,tmp):

        if start is None:
            return
        if start.left!=None and start.right!=None:
            tmp.append(start.value)
        self.GetFullNodes(start.left,tmp)
        self.GetFullNodes(start.right,tmp)

    def PrintFullNodesBinaryTree(self):

        start=self.root
        tmp=[]
        self.GetFullNodes(start,tmp)
        return tmp


def main():

    tree=BinaryTree(10)
    tree.root.left=Node(8)
    tree.root.right=Node(2)
    tree.root.left.left=Node(3)
    tree.root.left.right=Node(5)
    tree.root.right.left = Node(7)
    print(tree.print_tree('preorder'))
    print(tree.PrintFullNodesBinaryTree())

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.right.left = Node(4)
    tree1.root.right.right = Node(6)
    print(tree1.print_tree('preorder'))
    print(tree1.PrintFullNodesBinaryTree())

if __name__=='__main__':
    main()