'''
Check if there is a root to leaf path with given sequence
Given a binary tree and an array, the task is to find if the given array sequence is present as a root to leaf path in given tree.

Examples :

Input : arr[] = {2, 4, 8} for above tree
Output: "Path Exist"

Input :  arr[] = {5, 3, 4, 9} & above tree
Output: "Path does not Exist"
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

    def RootToleafGivenSequence(self,start,tmp,fnl_lst):

        if start.left is None and start.right is None:
            tmp.append(str(start.value))
            fnl_lst.append(tmp.copy())
            return
        tmp.append(str(start.value))
        self.RootToleafGivenSequence(start.left,tmp,fnl_lst)
        tmp.pop()
        self.RootToleafGivenSequence(start.right,tmp,fnl_lst)
        tmp.pop()


    def RootToLeafGivenSequenceBinaryTree(self,ary):

        start=self.root
        tmp=[]
        fnl_lst=[]
        self.RootToleafGivenSequence(start,tmp,fnl_lst)
        lst=[]
        for key in ary:
            lst.append(str(key))
        flg=False
        for key in fnl_lst:
            try:
                idx=''.join(key).index(''.join(lst))
            except:
                idx=-1
            if idx!=-1:
                flg=True
                break
        return flg

def main():

    tree=BinaryTree(5)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(4)
    tree.root.left.right.left = Node(6)
    tree.root.left.right.right = Node(8)
    print(tree.print_tree('preorder'))
    ary=[2,4,8]
    print(tree.RootToLeafGivenSequenceBinaryTree(ary))
    ary = [5,3,4,9]
    print(tree.RootToLeafGivenSequenceBinaryTree(ary))


if __name__=='__main__':
    main()