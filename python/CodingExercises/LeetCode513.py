'''
513. Find Bottom Left Tree Value
Given a binary tree, find the leftmost value in the last row of the tree.
Example 1:
Input:

    2
   / \
  1   3
Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
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

    def LeetCode513(self):
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
                if node.left!=None:
                    tmp.append(node.left.data)
                if node.left!=None:
                    node_lst.append(node.left)
                if node.right!=None:
                    node_lst.append(node.right)
            height=height+1
            if len(tmp)!=0:
                dict[height]=tmp
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            node_lst.append('NONE')
            node_lst.pop(0)
        return sorted(dict.items(),key=lambda x:x[0],reverse=True)[0][1][0]

def main():

    tree=BinaryTree(2)
    tree.root.left=Node(1)
    tree.root.right=Node(3)
    print(tree.PrintPreorder())
    print(tree.LeetCode513())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(6)
    tree.root.right.left.left = Node(7)
    print(tree.PrintPreorder())
    print(tree.LeetCode513())

if __name__=='__main__':
    main()