'''
1325. Delete Leaves With a Given Value
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target,
it should also be deleted (you need to continue doing that until you can't).
Example 1:
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left).
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:
Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:
Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
Example 4:
Input: root = [1,1,1], target = 1
Output: []
Example 5:
Input: root = [1,2,3], target = 1
Output: [1,2,3]
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

    def DeleteLeaves(self,start, target):
        if start is None:
            return None
        start.left=self.DeleteLeaves(start.left,target)
        start.right=self.DeleteLeaves(start.right,target)

        if start.left is None and start.right is None:
            if start.value==target:
                return None
        return start

    def DeleteLeavesGivenValue(self,target):
        start=self.root
        self.DeleteLeaves(start,target)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(2)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(4)
    print(tree.PrintTree())
    target=2
    print(tree.DeleteLeavesGivenValue(target))
    print(tree.PrintTree())
    
if __name__=='__main__':
    main()