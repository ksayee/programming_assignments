'''
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
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

    def print_tree(self,traversal_type):
        start=self.root
        tmp=[]
        if traversal_type=='preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)

    def LeetCode111(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        tmp=[]
        tmp.append(start.value)
        height=1
        dict={}
        dict[height]=tmp

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    if n.left.left is None and n.left.right is None:
                        tmp.append(n.left.value)
                if n.right!= None:
                    if n.right.left is None and n.right.right is None:
                        tmp.append(n.right.value)

                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append('NONE')
        sort_lst=sorted(dict.items(),key=lambda x:x[0])
        for i in range(1,len(sort_lst)):
            key=sort_lst[i]
            if len(key[1])>0:
                return key[0]

def main():

    tree1=BinaryTree(3)
    tree1.root.left=Node(9)
    tree1.root.right=Node(20)
    tree1.root.right.left=Node(15)
    tree1.root.right.right = Node(7)
    print(tree1.print_tree('preorder'))
    print(tree1.LeetCode111())

if __name__=='__main__':
    main()