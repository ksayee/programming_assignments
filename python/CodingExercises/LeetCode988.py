'''
988. Smallest String Starting From Leaf
Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents 'b', and so on.
Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def GetRootToLeaf(self,start,tmp,output_lst):
        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
            tmp.reverse()
            output_lst.append(''.join(tmp))
            tmp.reverse()
            tmp.pop()
            return
        tmp.append(start.value)
        self.GetRootToLeaf(start.left,tmp,output_lst)
        self.GetRootToLeaf(start.right,tmp,output_lst)
        tmp.pop()

    def SmallestStringStartingFromLeaf(self):
        start=self.root
        output_lst=[]
        tmp=[]
        self.GetRootToLeaf(start,tmp,output_lst)
        return sorted(output_lst)[0]

def main():

    tree=BinaryTree('a')
    tree.root.left=Node('b')
    tree.root.right = Node('c')
    tree.root.left.left = Node('d')
    tree.root.left.right = Node('e')
    tree.root.right.left = Node('d')
    tree.root.right.right = Node('e')
    print(tree.PrintTree())
    print(tree.SmallestStringStartingFromLeaf())

    tree = BinaryTree('z')
    tree.root.left = Node('b')
    tree.root.right = Node('d')
    tree.root.left.left = Node('b')
    tree.root.left.right = Node('d')
    tree.root.right.left = Node('a')
    tree.root.right.right = Node('c')
    print(tree.PrintTree())
    print(tree.SmallestStringStartingFromLeaf())

    tree = BinaryTree('c')
    tree.root.left = Node('c')
    tree.root.right = Node('b')
    tree.root.left.right = Node('b')
    tree.root.left.right.left = Node('a')
    tree.root.right.left = Node('a')
    print(tree.PrintTree())
    print(tree.SmallestStringStartingFromLeaf())

if __name__=='__main__':
    main()