'''
129. Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
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
        if start is None:
            return
        tmp.append(start.value)
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)


    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            tmp=[]
            start=self.root
            self.preorder(start,tmp)
            return tmp

    def GetNumbersRootToLeaf(self,start,tmp,fnl_lst):

        if start.left is None and start.right is None:
            tmp.append(str(start.value))
            fnl_lst.append(''.join(tmp))
            return
        tmp.append(str(start.value))
        self.GetNumbersRootToLeaf(start.left, tmp, fnl_lst)
        tmp.pop()
        self.GetNumbersRootToLeaf(start.right, tmp, fnl_lst)
        tmp.pop()

    def LeetCode129(self):

        start=self.root
        tmp=[]
        fnl_lst=[]
        self.GetNumbersRootToLeaf(start,tmp,fnl_lst)

        sum=0
        for l in fnl_lst:
            sum=sum+int(l)
        return sum

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    print(tree.print_tree('preorder'))
    print(tree.LeetCode129())

    tree1 = BinaryTree(4)
    tree1.root.left = Node(9)
    tree1.root.right = Node(0)
    tree1.root.left.left=Node(5)
    tree1.root.left.right=Node(1)
    print(tree1.print_tree('preorder'))
    print(tree1.LeetCode129())

if __name__=='__main__':
    main()