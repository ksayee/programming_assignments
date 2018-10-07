'''
Print all nodes that are at distance k from a leaf node
Given a Binary Tree and a positive integer k, print all nodes that are distance k from a leaf node.
Here the meaning of distance is different from previous post.
Here k distance from a leaf means k levels higher than a leaf node. For example if k is more than height of Binary Tree,
then nothing should be printed. Expected time complexity is O(n) where n is the number nodes in the given Binary Tree.
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

    def GetLeaves(self,start):

        node_lst=[]
        node_lst.append(start)
        height=0
        node_lst.append('NONE')
        leaf_lst=[]

        while len(node_lst)!=0:
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                if n.left is None and n.right is None:
                    tup=(n.value,height)
                    leaf_lst.append(tup)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            node_lst.pop(0)
            node_lst.append('NONE')
            height=height+1
        return leaf_lst

    def PrintNodesKDistanceFromLeafNodesBinaryTree(self,k):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=0
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[height]=tmp

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    tmp.append(n.left.value)
                    node_lst.append(n.left)
                if n.right!=None:
                    tmp.append(n.right.value)
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            fnl_dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")

        leaf_lst=self.GetLeaves(start)
        out_lst=[]
        for key in leaf_lst:
            val=abs(key[1]-k)
            if val in fnl_dict.keys():
                lst=fnl_dict[val]
                for l in lst:
                    if key[0]!=l:
                        out_lst.append(l)
        return list(set(out_lst))





            
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left= Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.left.right = Node(8)
    print(tree.print_tree('preorder'))
    k=2
    print(tree.PrintNodesKDistanceFromLeafNodesBinaryTree(k))

if __name__=='__main__':
    main()