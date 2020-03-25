'''
1080. Insufficient Nodes in Root to Leaf Paths
Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)
A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.
Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.
Example 1:
Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:
Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:
Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]
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
        return '#'.join(tmp)

    def NodeRootToLeaf(self,start,limit,sum):
        if start is None:
            return
        sum=sum+start.value
        start.left=self.NodeRootToLeaf(start.left,limit,sum)
        start.right=self.NodeRootToLeaf(start.right,limit,sum)

        if start.left is None and start.right is None:
            if sum<limit:
                return None
            else:
                return start
        return start

    def InsufficientNodeRootToLeaf(self,limit):
        start=self.root
        sum=0
        self.NodeRootToLeaf(start,limit,sum)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(-99)
    tree.root.left.left.left = Node(8)
    tree.root.left.left.right = Node(9)
    tree.root.left.right.left = Node(-99)
    tree.root.left.right.right = Node(-99)
    tree.root.right.left = Node(-99)
    tree.root.right.right = Node(7)
    tree.root.right.left.left = Node(12)
    tree.root.right.left.right = Node(13)
    tree.root.right.right.left = Node(-99)
    tree.root.right.right.right = Node(14)
    print(tree.PrintTree())
    limit=1
    tree.InsufficientNodeRootToLeaf(limit)
    print(tree.PrintTree())

    tree = BinaryTree(5)
    tree.root.left = Node(4)
    tree.root.right = Node(8)
    tree.root.left.left = Node(11)
    tree.root.left.left.left = Node(7)
    tree.root.left.left.right = Node(1)
    tree.root.right.left = Node(17)
    tree.root.right.right = Node(4)
    tree.root.right.right.left = Node(5)
    tree.root.right.right.right = Node(3)
    print(tree.PrintTree())
    limit = 22
    tree.InsufficientNodeRootToLeaf(limit)
    print(tree.PrintTree())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(-3)
    tree.root.left.left = Node(-5)
    tree.root.right.left = Node(4)
    print(tree.PrintTree())
    limit = -1
    tree.InsufficientNodeRootToLeaf(limit)
    print(tree.PrintTree())

if __name__=='__main__':
    main()