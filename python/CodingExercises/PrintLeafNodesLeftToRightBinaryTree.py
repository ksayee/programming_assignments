# Sum of all elements in a binary tree

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

    def LeafNodesLefttoRight(self,start,tmp):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
        self.LeafNodesLefttoRight(start.left,tmp)
        self.LeafNodesLefttoRight(start.right,tmp)

    def PrintLeafNodesLeftToRightBinaryTree(self):

        start=self.root
        tmp=[]
        self.LeafNodesLefttoRight(start,tmp)
        return tmp

def main():

    tree1=BinaryTree(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)
    tree1.root.left.left=Node(4)
    tree1.root.right.left=Node(5)
    tree1.root.right.left.left = Node(6)
    tree1.root.right.left.right = Node(7)
    tree1.root.right.right = Node(8)
    tree1.root.right.right.left = Node(9)
    tree1.root.right.right.right = Node(10)
    print(tree1.print_tree('preorder'))
    print(tree1.PrintLeafNodesLeftToRightBinaryTree())

if __name__=='__main__':
    main()