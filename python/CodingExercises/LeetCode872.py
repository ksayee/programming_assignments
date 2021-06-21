'''
872. Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
Example 1:
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:
Input: root1 = [1], root2 = [1]
Output: true
Example 3:
Input: root1 = [1], root2 = [2]
Output: false
Example 4:
Input: root1 = [1,2], root2 = [2,2]
Output: true
Example 5:
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
'''

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,value):
        self.root = Node(value)

    def GetLeafs(self,start,tmp):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
        self.GetLeafs(start.left,tmp)
        self.GetLeafs(start.right,tmp)

    def LeafSimilarTrees(self,tree):

        start1 = self.root
        start2 = tree.root
        tree1_leafs = []
        tree2_leafs = []

        self.GetLeafs(start1,tree1_leafs)
        self.GetLeafs(start2,tree2_leafs)
        print(tree1_leafs)
        print(tree2_leafs)

        if tree1_leafs == tree2_leafs:
            return True
        else:
            return False

def main():

    tree1 = BinaryTree(3)
    tree1.root.left = Node(5)
    tree1.root.right = Node(1)
    tree1.root.left.left = Node(6)
    tree1.root.left.right = Node(2)
    tree1.root.left.right.left = Node(7)
    tree1.root.left.right.right = Node(4)
    tree1.root.right.left = Node(9)
    tree1.root.right.right = Node(8)

    tree2 = BinaryTree(3)
    tree2.root.left = Node(5)
    tree2.root.right = Node(1)
    tree2.root.left.left = Node(6)
    tree2.root.left.right = Node(7)
    tree2.root.right.left = Node(4)
    tree2.root.right.right = Node(2)
    tree2.root.right.right.left = Node(9)
    tree2.root.right.right.right = Node(8)
    print(tree1.LeafSimilarTrees(tree2))

if __name__=='__main__':
    main()