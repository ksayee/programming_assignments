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
        tmp.append(str(start.value)+'-')
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)


    def print_tree(self,traversal_type):
        tmp=[]
        if traversal_type=='preorder':
            self.preorder(self.root,tmp)
            return ''.join(tmp)
        elif traversal_type=='inorder':
            return self.inorder(self.root,tmp)
        elif traversal_type=='postorder':
            return self.postorder(self.root,tmp)

    def SumFunction(self,start):

        if start is None:
            return 0
        return self.SumFunction(start.left)+start.value+self.SumFunction(start.right)

    def CheckSumTree(self,start):

        if start is None:
            return True
        if start.left is None and start.right is None:
            return True

        left=self.SumFunction(start.left)
        right=self.SumFunction(start.right)
        if start.value==left+right:
            if self.CheckSumTree(start.left)==True and self.CheckSumTree(start.right)==True:
                return True
        else:
            return False

    def SumTreeBinaryTree(self):

        start=self.root
        flg=self.CheckSumTree(start)
        return flg

def main():

    tree=BinaryTree(26)
    tree.root.left=Node(10)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(6)
    tree.root.right.right=Node(3)
    print(tree.print_tree('preorder'))
    print(tree.SumTreeBinaryTree())

if __name__=='__main__':
    main()