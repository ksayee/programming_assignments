'''
222. Count Complete Tree Nodes
Medium
Given a complete binary tree, count the number of nodes.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Example:
Input:
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
'''

import math

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

    def PrintPreorder(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def LevelOrderTraversal(self):
        start=self.root
        nodes=[]
        dict={}
        height=1
        nodes.append(start)
        nodes.append('NONE')
        tmp=[]
        tmp.append(start.value)
        dict[height]=tmp

        while len(nodes)>0:
            tmp=[]
            while nodes[0]!='NONE':
                n=nodes[0]
                nodes.pop(0)
                if n.left!=None:
                    tmp.append(n.left.value)
                    nodes.append(n.left)
                else:
                    tmp.append('NULL')
                if n.right!=None:
                    tmp.append(n.right.value)
                    nodes.append(n.right)
                else:
                    tmp.append('NULL')
            height=height+1
            dict[height]=tmp
            if nodes[-1]=='NONE' and len(nodes)==1:
                break
            nodes.pop(0)
            nodes.append('NONE')

        del dict[height]
        return dict

    def CheckCompleteBinaryTree(self):

        dict=self.LevelOrderTraversal()
        print(dict.items())
        sort_dict=sorted(dict.items(),key=lambda x:x[0],reverse=True)
        flg=True
        for i in range(1,len(sort_dict)):
            val=sort_dict[i][1]
            for l in val:
                if l=='NULL':
                    flg=False
                    break
            if flg==False:
                break

        if flg==True:
            val=sort_dict[0][1]
            for l in val:
                if l=='NULL' and flg==False:
                    pass
                elif l=='NULL' and flg==True:
                    flg=False
                elif l!='NULL' and flg==False:
                    return False
                else:
                    flg=True
            return True
        else:
            return False

    def ReturnNumOfNodes(self):

        if self.CheckCompleteBinaryTree()==True:
            dict=self.LevelOrderTraversal()
            cnt=0
            for key,val in dict.items():
                for node in val:
                    if node!='NULL':
                        cnt=cnt+1
            return cnt
        else:
            return 0

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    print(tree.PrintPreorder())
    print(tree.CheckCompleteBinaryTree())
    print(tree.ReturnNumOfNodes())

if __name__=='__main__':
    main()