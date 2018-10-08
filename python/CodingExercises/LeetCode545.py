'''
545. Boundary of Binary Tree
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1
Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2
Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
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

    def inorder(self,start,tmp):

        if start is None:
            return
        self.inorder(start.left,tmp)
        tmp.append(str(start.value))
        self.inorder(start.right,tmp)

    def PrintTree(self,traversal):

        start = self.root
        tmp = []
        if traversal=='Preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)
        if traversal=='Inorder':
            self.inorder(start,tmp)
            return '-'.join(tmp)

    def GetLeafNodes(self,start,leaf_lst):

        if start is None:
            return
        if start.left is None and start.right is None:
            leaf_lst.append(start.value)
        self.GetLeafNodes(start.left,leaf_lst)
        self.GetLeafNodes(start.right,leaf_lst)

    def LeetCode545(self):

        start=self.root
        leaf_lst=[]
        self.GetLeafNodes(start,leaf_lst)

        node_lst=[]
        node_lst.append(start)
        height=1
        tmp=[]
        tmp.append(start.value)
        dict={}
        dict[height]=tmp
        node_lst.append("NONE")

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    node_lst.append(n.left)
                    tmp.append(n.left.value)
                if n.right!=None:
                    node_lst.append(n.right)
                    tmp.append(n.right.value)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")

        out_lst=[]
        sort_lst=sorted(dict.items(),key=lambda x:x[0])

        for key in sort_lst:
            out_lst.append(key[1][0])
        for l in leaf_lst:
            if l not in out_lst:
                out_lst.append(l)
        sort_lst = sorted(dict.items(), key=lambda x: x[0],reverse=True)
        for key in sort_lst:
            if key[1][-1] not in out_lst:
                out_lst.append(key[1][-1])

        return out_lst
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left= Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(8)
    tree.root.right.left = Node(6)
    tree.root.right.left.left = Node(9)
    tree.root.right.left.right = Node(10)
    print(tree.PrintTree("Preorder"))
    print(tree.LeetCode545())

if __name__=='__main__':
    main()