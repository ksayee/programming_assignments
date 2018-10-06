'''
Check if two nodes are cousins in a Binary Tree
Given the binary Tree and the two nodes say ‘a’ and ‘b’, determine whether the two nodes are cousins of each other or not.
Two nodes are cousins of each other if they are at same level and have different parents.

Example

     6
   /   \
  3     5
 / \   / \
7   8 1   3
Say two node be 7 and 1, result is TRUE.
Say two nodes are 3 and 5, result is FALSE.
Say two nodes are 7 and 5, result is FALSE.
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

    def CheckCousin(self,start,n):

        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=0
        found=False
        parent=-1
        while len(node_lst)!=0:
            while node_lst[0]!="NONE":
                nd=node_lst[0]
                node_lst.pop(0)
                if nd.left!=None and nd.left.value==n:
                    parent=nd.value
                    found=True
                    break
                if nd.right!=None and nd.right.value==n:
                    parent=nd.value
                    found=True
                    break
                if nd.left!=None:
                    node_lst.append(nd.left)
                if nd.right!=None:
                    node_lst.append(nd.right)
            height=height+1
            if found==True:
                break
            if  node_lst[0]=='NONE' and len(node_lst)==1:
                break
            node_lst.pop(0)
            node_lst.append("NONE")
        tup=(parent,height)

        return tup

    def CousinsBinaryTree(self,n1,n2):

        start=self.root
        n1_tup=self.CheckCousin(start,n1)
        n2_tup=self.CheckCousin(start,n2)
        print(n1_tup,n2_tup)
        if n1_tup[0]!=n2_tup[0] and n1_tup[1]==n2_tup[1]:
            return True
        else:
            return False

def main():

    tree=BinaryTree(6)
    tree.root.left=Node(3)
    tree.root.right=Node(5)
    tree.root.left.left=Node(7)
    tree.root.left.right = Node(8)
    tree.root.right.left = Node(1)
    tree.root.right.right = Node(3)
    print(tree.print_tree('preorder'))
    n1=7
    n2=1
    print(tree.CousinsBinaryTree(n1,n2))
    n1 = 3
    n2 = 5
    print(tree.CousinsBinaryTree(n1, n2))
    n1 = 7
    n2 = 5
    print(tree.CousinsBinaryTree(n1, n2))

if __name__=='__main__':
    main()