# Construct a Binary Tree in Python.

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

    def inorder(self,start,traversal):
        if start!=None:
            traversal = self.preorder(start.left, traversal)
            traversal=traversal+ (str(start.value)+ '-')
            traversal = self.preorder(start.right, traversal)
        return traversal

    def postorder(self,start,traversal):
        if start!=None:
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
            traversal = traversal + (str(start.value) + '-')
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(self.root,'')
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    tree.root.right.right.right=Node(8)
    print(tree.print_tree('preorder'))
    print(tree.print_tree('inorder'))
    print(tree.print_tree('postorder'))

if __name__=='__main__':
    main()