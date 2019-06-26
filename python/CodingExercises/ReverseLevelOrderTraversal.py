'''
Reverse Level Order Traversal
We have discussed level order traversal of a post in previous post. The idea is to print last level first, then second last level, and so on. Like Level order traversal, every level is printed from left to right.
Example Tree
Example Tree

Reverse Level order traversal of the above tree is “4 5 2 3 1”.

Both methods for normal level order traversal can be easily modified to do reverse level order traversal.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.PreOrder(start.left,tmp)
        self.PreOrder(start.right,tmp)

    def PrintPreOrder(self):
        tmp=[]
        start=self.root
        self.PreOrder(start,tmp)
        return '-'.join(tmp)

    def ReverseLevelOrderTraversal(self):
        start=self.root
        dict={}
        height=1
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                tmp.append(n.value)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            dict[height]=tmp
            height=height+1
            node_lst.pop(0)
            node_lst.append("NONE")
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
        sort_dict=sorted(dict.items(),key=lambda x:x[0],reverse=True)
        fnl_lst=[]
        for tup in sort_dict:
            val=tup[1]
            for v in val:
                fnl_lst.append(str(v))
        return '-'.join(fnl_lst)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    print(tree.PrintPreOrder())
    print(tree.ReverseLevelOrderTraversal())

if __name__=='__main__':
    main()