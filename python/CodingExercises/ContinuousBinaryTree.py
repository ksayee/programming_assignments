'''
Continuous Tree
A tree is Continuous tree if in each root to leaf path,
absolute difference between keys of two adjacent is 1.
We are given a binary tree, we need to check if tree is continuous or not.
Examples:
Input :              3
                    / \
                   2   4
                  / \   \
                 1   3   5
Output: "Yes"
// 3->2->1 every two adjacent node's absolute difference is 1
// 3->2->3 every two adjacent node's absolute difference is 1
// 3->4->5 every two adjacent node's absolute difference is 1
Input :              7
                    / \
                   5   8
                  / \   \
                 6   4   10
Output: "No"
// 7->5->6 here absolute difference of 7 and 5 is not 1.
// 7->5->4 here absolute difference of 7 and 5 is not 1.
// 7->8->10 here absolute difference of 8 and 10 is not 1.
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.data))
        self.PreOrder(start.left,tmp)
        self.PreOrder(start.right,tmp)

    def CheckContinuousBinaryTree(self,start,tmp,flg_lst):
        if start is None:
            return
        tmp.append(start.data)
        if start.left is None and start.right is None:
            for i in range(1,len(tmp)):
                if abs(tmp[i]-tmp[i-1])>1:
                    flg_lst.append(False)
                else:
                    flg_lst.append(True)
        self.CheckContinuousBinaryTree(start.left,tmp,flg_lst)
        self.CheckContinuousBinaryTree(start.right,tmp,flg_lst)
        tmp.pop()

    def ContinuousBinaryTree(self):
        start=self.root
        tmp=[]
        flg_lst=[]
        self.CheckContinuousBinaryTree(start,tmp,flg_lst)
        if False in flg_lst:
            return False
        else:
            return True

def main():

    tree=BinaryTree(3)
    tree.root.left=Node(2)
    tree.root.right = Node(4)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(5)
    print(tree.ContinuousBinaryTree())

    tree = BinaryTree(7)
    tree.root.left = Node(5)
    tree.root.right = Node(8)
    tree.root.left.left = Node(6)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(10)
    print(tree.ContinuousBinaryTree())

if __name__=='__main__':
    main()