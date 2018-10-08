'''
199. Binary Tree Right Side View
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
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

    def inorder(self,start,tmp):

        if start is None:
            return
        self.inorder(start.left,tmp)
        tmp.append(str(start.value))
        self.inorder(start.right,tmp)

    def PrintTree(self,traversal):

        start = self.root
        tmp = []
        if traversal=='Preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)
        if traversal=='Inorder':
            self.inorder(start,tmp)
            return '-'.join(tmp)

    def LeetCode199(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        height=1
        tmp=[]
        tmp.append(start.value)
        dict={}
        dict[height]=tmp
        node_lst.append("NONE")

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    node_lst.append(n.left)
                    tmp.append(n.left.value)
                if n.right!=None:
                    node_lst.append(n.right)
                    tmp.append(n.right.value)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")

        out_lst=[]
        sort_lst=sorted(dict.items(),key=lambda x:x[0])

        for key in sort_lst:
            if key[1][-1] not in out_lst:
                out_lst.append(key[1][-1])

        return out_lst
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(4)
    print(tree.PrintTree("Preorder"))
    print(tree.LeetCode199())

if __name__=='__main__':
    main()