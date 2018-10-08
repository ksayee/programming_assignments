'''
Find depth of the deepest odd level leaf node
Write a C code to get the depth of the deepest odd level leaf node in a binary tree. Consider that level starts with 1. Depth of a leaf node is number of nodes on the path from root to leaf (including both leaf and root).

For example, consider the following tree. The deepest odd level node is the node with value 9 and depth of this node is 5.

       1
     /   \
    2     3
  /      /  \
 4      5    6
        \     \
         7     8
        /       \
       9         10
                 /
                11
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

    def DepthDeepestOddLevelLeafNodeBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        height=1
        tmp=[]
        dict={}
        dict[height]=tmp
        node_lst.append("NONE")

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    if n.left.left is None and n.left.right is None:
                        tmp.append(n.left.value)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")

        sort_lst=sorted(dict.items(),key=lambda x:x[0],reverse=True)

        for key in sort_lst:
            if key[0]%2!=0 and len(key[1])>0:
                return key[1]
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.left.right = Node(7)
    tree.root.right.left.right.left = Node(9)
    tree.root.right.right.right = Node(8)
    tree.root.right.right.right.right = Node(10)
    tree.root.right.right.right.right.left = Node(11)
    print(tree.PrintTree("Preorder"))
    print(tree.DepthDeepestOddLevelLeafNodeBinaryTree())

if __name__=='__main__':
    main()