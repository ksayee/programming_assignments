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

    def postorder(self,start,tmp):
        if start==None:
            return
        self.postorder(start.left,tmp)
        self.postorder(start.right,tmp)
        tmp.append(str(start.value))

    def print_tree(self,traversal):
        if traversal=='postorder':
            start=self.root
            tmp=[]
            self.postorder(start,tmp)
        return '-'.join(tmp)

    def PostOrderTraversalIterativeBinaryTree(self):

        start=self.root

        stk1=[]
        stk2=[]
        tmp=[]

        stk1.append(start)

        while len(stk1)>0:
            stk2.append(stk1[-1])
            n=stk1[-1]
            stk1.pop()
            if n.left!=None:
                stk1.append(n.left)
            if n.right!=None:
                stk1.append(n.right)

        while len(stk2)!=0:
            n=stk2[-1]
            stk2.pop()
            tmp.append(str(n.value))
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
    print(tree.print_tree('postorder'))
    print(tree.PostOrderTraversalIterativeBinaryTree())

if __name__=='__main__':
    main()