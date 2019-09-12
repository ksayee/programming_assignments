'''
Check whether a given Binary Tree is Complete or not | Set 1 (Iterative Solution)
Given a Binary Tree, write a function to check whether the given Binary Tree is Complete Binary Tree or not.
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. See the following examples.

The following trees are examples of Complete Binary Trees
    1
  /   \
 2     3

       1
    /    \
   2       3
  /
 4

       1
    /    \
   2      3
  /  \    /
 4    5  6
The following trees are examples of Non-Complete Binary Trees
    1
      \
       3

       1
    /    \
   2       3
    \     /  \
     4   5    6

       1
    /    \
   2      3
         /  \
        4    5
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def CheckBinaryTreeCompleteOrNot(self):

        queue=[]
        start=self.root
        queue.append(start)
        flg=True
        while len(queue)!=0:
            node=queue[0]
            queue.pop(0)
            if node.left!=None:
                if flg==False:
                    return False
                queue.append(node.left)
            else:
                flg=False
            if node.right!=None:
                if flg==False:
                    return False
                queue.append(node.right)
            else:
                flg=False
        return True

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    print(tree.CheckBinaryTreeCompleteOrNot())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    print(tree.CheckBinaryTreeCompleteOrNot())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left=Node(6)
    print(tree.CheckBinaryTreeCompleteOrNot())

    tree = BinaryTree(1)
    tree.root.right = Node(3)
    print(tree.CheckBinaryTreeCompleteOrNot())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(6)
    print(tree.CheckBinaryTreeCompleteOrNot())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    print(tree.CheckBinaryTreeCompleteOrNot())

if __name__=='__main__':
    main()