'''
257. Binary Tree Paths
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.
Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
        tmp.append(str(start.value))
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def PrintTree(self,traversal):

        if traversal=='Preorder':
            start=self.root
            tmp=[]
            self.preorder(start,tmp)
            return '-'.join(tmp)

    def PrintRootToLeaf(self,start,tmp):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(str(start.value))
            print('-'.join(tmp))
            tmp.pop()
        tmp.append(str(start.value))
        self.PrintRootToLeaf(start.left,tmp)
        self.PrintRootToLeaf(start.right,tmp)
        tmp.pop()

    def LeetCode257(self):

        start=self.root
        tmp=[]
        self.PrintRootToLeaf(start,tmp)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.right = Node(5)
    print(tree.PrintTree("Preorder"))
    tree.LeetCode257()

if __name__=='__main__':
    main()