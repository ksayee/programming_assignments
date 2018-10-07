'''
Deepest left leaf node in a binary tree
Given a Binary Tree, find the deepest leaf node that is left child of its parent. For example, consider the following tree. The deepest left leaf node is the node with value 9.
       1
     /   \
    2     3
  /      /  \
 4      5    6
        \     \
         7     8
        /       \
       9         10
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
        if start==None:
            return
        tmp.append(str(start.value))
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def print_tree(self,traversal):
        if traversal=='preorder':
            start=self.root
            tmp=[]
            self.preorder(start,tmp)
        return '-'.join(tmp)

    def DeepestLeftLeafNodeBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=1
        dict={}
        tmp=[]

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    if n.left.left is None and n.left.right is None:
                        tmp.append(n.left.value)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if node_lst[0]=="NONE" and len(node_lst)==1:
                break
            if len(tmp)>0:
                height=height+1
                dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")

        sort_lst=sorted(dict.items(),key=lambda x:x[0],reverse=True)

        return sort_lst[0][1]

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.left.right = Node(7)
    tree.root.right.left.right.left = Node(9)
    tree.root.right.right.right = Node(8)
    tree.root.right.right.right.right = Node(10)
    print(tree.print_tree('preorder'))
    print(tree.DeepestLeftLeafNodeBinaryTree())


if __name__=='__main__':
    main()