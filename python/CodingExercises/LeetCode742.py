'''
Given a binary tree where every node has a unique value, and a target key k, find the closest leaf node to target k in the tree.
A node is called a leaf if it has no children.
In the following examples, the input tree is represented in flattened form row by row. The actual roottree given will be a TreeNode object.
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6
Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is closest to the node with value 2.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def ClosestLeafToNode(self,k):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        height=0
        node_lst.append('NONE')
        flg=False
        node_height=-1
        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.value==k:
                    flg=True
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
                if n.left is None and n.right is None:
                    tmp.append(n.value)
            height=height+1
            dict[height]=tmp.copy()
            if flg==True:
                node_height=height
                flg=False
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            else:
                node_lst.append('NONE')
                node_lst.pop(0)
        max_diff=999
        for key,val in dict.items():
            if abs(node_height-key)<max_diff:
                max_diff=abs(node_height-key)
                leaf=dict[key]
        return leaf
    
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.left.left = Node(5)
    tree.root.left.left.left.left = Node(6)
    print(tree.PrintTree())
    k=2
    print(tree.ClosestLeafToNode(k))

if __name__=='__main__':
    main()