'''
Print all nodes that don’t have sibling
Given a Binary Tree, print all nodes that don’t have a sibling (a sibling is a node that has same parent. In a Binary Tree, there can be at most one sibling). Root should not be printed as root cannot have a sibling.

For example, the output should be “4 5 6” for the following tree.

Binary Tree
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

    def NodesNoSiblings(self,start,tmp):
        if start is None:
            return
        if start.left !=None or start.right!=None:
            if start.left is None and start.right!=None:
                tmp.append(start.right.value)
            if start.left!=None and start.right is None:
                tmp.append(start.left.value)
        self.NodesNoSiblings(start.left,tmp)
        self.NodesNoSiblings(start.right,tmp)

    def NodesNoSiblingsBinaryTree(self):

        start=self.root
        tmp=[]
        self.NodesNoSiblings(start,tmp)
        return tmp


def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(5)
    tree.root.right.left.left = Node(6)
    print(tree.print_tree('preorder'))
    print(tree.NodesNoSiblingsBinaryTree())

if __name__=='__main__':
    main()