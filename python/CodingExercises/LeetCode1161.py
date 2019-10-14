'''
1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
Example 1:
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.data))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintPreorder(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def LeetCode1161(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        height=0
        node_lst.append("NONE")

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                node=node_lst[0]
                node_lst.pop(0)
                tmp.append(node.data)
                if node.left!=None:
                    node_lst.append(node.left)
                if node.right!=None:
                    node_lst.append(node.right)
            sum=0
            for item in tmp:
                sum=sum+item
            height=height+1
            dict[height]=sum
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            node_lst.append('NONE')
            node_lst.pop(0)
        return sorted(dict.items(),key=lambda x:x[1],reverse=True)[0][0]

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(7)
    tree.root.right=Node(0)
    tree.root.left.left=Node(7)
    tree.root.left.right=Node(-8)
    print(tree.PrintPreorder())
    print(tree.LeetCode1161())

if __name__=='__main__':
    main()