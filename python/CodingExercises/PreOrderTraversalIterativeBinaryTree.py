'''
Iterative Preorder Traversal
Given a Binary Tree, write an iterative function to print Preorder traversal of the given binary tree.
Refer this for recursive preorder traversal of Binary Tree. To convert an inherently recursive procedures to iterative, we need an explicit stack. Following is a simple stack based iterative process to print Preorder traversal.
1) Create an empty stack nodeStack and push root node to stack.
2) Do following while nodeStack is not empty.
….a) Pop an item from stack and print it.
….b) Push right child of popped item to stack
….c) Push left child of popped item to stack
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

    def PreOrderTraversalIterativeBinaryTree(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        tmp=[]
        while len(node_lst)!=0:
            n=node_lst.pop()
            tmp.append(str(n.value))
            if n.right!=None:
                node_lst.append(n.right)
            if n.left!=None:
                node_lst.append(n.left)
        return '-'.join(tmp)

def main():

    tree=BinaryTree(6)
    tree.root.left=Node(3)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(5)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(4)
    tree.root.right.right = Node(4)
    print(tree.print_tree('preorder'))
    print(tree.PreOrderTraversalIterativeBinaryTree())

if __name__=='__main__':
    main()