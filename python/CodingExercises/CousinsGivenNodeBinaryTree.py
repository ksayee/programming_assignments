'''
Print cousins of a given node in Binary Tree
Given a binary tree and a node, print all cousins of given node. Note that siblings should not be printed.

Example:

Input : root of below tree
             1
           /   \
          2     3
        /   \  /  \
       4    5  6   7
       and pointer to a node say 5.

Output : 6, 7
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

    def GetNodeParentHeight(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        height=0
        fnl_lst=[]
        while len(node_lst)!=0:
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n==self.root:
                    tup=(n.value,-1,-1)
                    fnl_lst.append(tup)
                if n.left!=None:
                    tup=(n.left.value,n.value,height)
                    fnl_lst.append(tup)
                if n.right!=None:
                    tup=(n.right.value,n.value,height)
                    fnl_lst.append(tup)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            height=height+1
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            node_lst.pop(0)
            node_lst.append('NONE')
        return fnl_lst

    def CousinsGivenNodeBinaryTree(self,n):

        fnl_lst=self.GetNodeParentHeight()
        hgt=0
        parent=0
        for key in fnl_lst:
            if key[0]==n:
                hgt=key[2]
                parent=key[1]
                break
        lst=[]
        for key in fnl_lst:
            if key[2]==hgt:
                if key[1]!=parent:
                    lst.append(key[0])
        return lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right= Node(7)
    print(tree.print_tree('preorder'))
    n=5
    print(tree.CousinsGivenNodeBinaryTree(n))

if __name__=='__main__':
    main()