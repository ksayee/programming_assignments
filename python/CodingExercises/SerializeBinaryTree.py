# Construct a Binary Tree in Python.

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
        if traversal_type=='preorder':
            tmp=[]
            start=self.root
            self.preorder(start,tmp)
            return ' '.join(tmp)
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def Serialize_recur(self,start,tmp):

        if start is None:
            tmp.append(str('#'))
            return
        tmp.append(str(start.value))
        self.Serialize_recur(start.left,tmp)
        self.Serialize_recur(start.right, tmp)

    def Serialize_tree(self):

        tmp=[]
        start=self.root
        self.Serialize_recur(start,tmp)
        return ' '.join(tmp)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    print(tree.print_tree('preorder'))
    print(tree.Serialize_tree())

    tree1 = BinaryTree(20)
    tree1.root.left = Node(8)
    tree1.root.right = Node(22)
    print(tree1.print_tree('preorder'))
    print(tree1.Serialize_tree())

    tree2 = BinaryTree(20)
    tree2.root.left = Node(8)
    tree2.root.left.left = Node(4)
    tree2.root.left.right = Node(12)
    tree2.root.left.right.left = Node(10)
    tree2.root.left.right.right = Node(14)
    print(tree2.print_tree('preorder'))
    print(tree2.Serialize_tree())

    tree3 = BinaryTree(20)
    tree3.root.left = Node(8)
    tree3.root.left.left = Node(10)
    tree3.root.left.left.left = Node(5)
    print(tree3.print_tree('preorder'))
    print(tree3.Serialize_tree())

if __name__=='__main__':
    main()