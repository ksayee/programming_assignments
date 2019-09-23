'''
Insertion in a Binary Tree in level order
Given a binary tree and a key, insert the key into the binary tree at first position available in level order.
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
The idea is to do iterative level order traversal of the given tree using queue.
If we find a node whose left child is empty, we make new key as left child of the node.
Else if we find a node whose right child is empty, we make new key as right child.
We keep traversing the tree until we find a node whose either left or right is empty.
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.data))
        self.PreOrder(start.left,tmp)
        self.PreOrder(start.right,tmp)

    def BinaryTreeInsertion(self,n):
        start=self.root
        tmp=[]
        self.PreOrder(start,tmp)
        print("Before Inserstion:",'-'.join(tmp))
        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        flg=False
        while len(node_lst)!=0:
            while node_lst[0]!="NONE":
                node=node_lst[0]
                node_lst.pop(0)
                if node.left!=None:
                    node_lst.append(node.left)
                else:
                    node.left=Node(n)
                    flg=True
                    break
                if flg==False:
                    if node.right!=None:
                        node_lst.append(node.right)
                    else:
                        node.right=Node(n)
                        flg=True
                        break
            if flg==True:
                break
            if node_lst[0]=="NONE" and len(node_lst)==1:
                break
            node_lst.pop(0)
            node_lst.append("NONE")
        start=self.root
        tmp=[]
        self.PreOrder(start,tmp)
        print("After Inserstion:",'-'.join(tmp))

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(11)
    tree.root.right = Node(9)
    tree.root.left.left = Node(7)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(8)
    n=12
    tree.BinaryTreeInsertion(n)

if __name__=='__main__':
    main()