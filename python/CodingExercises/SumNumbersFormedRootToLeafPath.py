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

    def SumNumbers_recur(self,start,tmp,fnl_lst):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(str(start.value))
            fnl_lst.append(int(''.join(tmp)))
            tmp.pop()
            return
        tmp.append(str(start.value))
        self.SumNumbers_recur(start.left,tmp,fnl_lst)
        self.SumNumbers_recur(start.right,tmp,fnl_lst)
        tmp.pop()

    def SumNumbersFormedRootToLeafPath(self):

        start=self.root
        tmp=[]
        fnl_lst=[]

        self.SumNumbers_recur(start,tmp,fnl_lst)
        sum=0
        for num in fnl_lst:
            sum=sum+num
        return sum


def main():

    tree=BinaryTree(6)
    tree.root.left=Node(3)
    tree.root.right=Node(5)
    tree.root.left.left=Node(2)
    tree.root.left.right=Node(5)
    tree.root.right.right=Node(4)
    tree.root.left.right.left=Node(7)
    tree.root.left.right.right = Node(4)
    print(tree.print_tree('preorder'))
    print(tree.SumNumbersFormedRootToLeafPath())

if __name__=='__main__':
    main()