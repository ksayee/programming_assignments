'''
958. Check Completeness of a Binary Tree
Medium
Given a binary tree, determine if it is a complete binary tree.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.
Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:
Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrderTraversal(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.PreOrderTraversal(start.left,tmp)
        self.PreOrderTraversal(start.right,tmp)

    def DisplayTree(self):
        start=self.root
        tmp=[]
        self.PreOrderTraversal(start,tmp)
        return '-'.join(tmp)

    def CheckCompleteness(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        flg=True
        while len(node_lst)!=0:
            node=node_lst[0]
            node_lst.pop(0)
            if node.left!=None:
                if flg==False:
                    return False
                node_lst.append(node.left)
            else:
                flg=False
            if node.right!=None:
                if flg==False:
                    return False
                node_lst.append(node.right)
            else:
                flg=False
        return True

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    print(tree.DisplayTree())
    print(tree.CheckCompleteness())

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree1.root.right.right = Node(7)
    print(tree1.DisplayTree())
    print(tree1.CheckCompleteness())

if __name__=='__main__':
    main()