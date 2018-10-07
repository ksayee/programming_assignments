'''
Given a Binary tree and a key in the binary tree, find the node right to the given key. If there is no node on right side, then return NULL. Expected time complexity is O(n) where n is the number of nodes in the given binary tree.

For example, consider the following Binary Tree. Output for 2 is 6, output for 4 is 5. Output for 10, 6 and 5 is NULL.

                  10
               /      \
             2         6
           /   \         \
         8      4          5
Input : 2
Output : 6

Input : 4
Output : 5
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

    def FindNextRightNodeBinaryTree(self,k):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=1
        dict={}
        tmp=[]
        tmp.append(start.value)
        dict[height]=tmp

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    tmp.append(n.left.value)
                    node_lst.append(n.left)
                if n.right!=None:
                    tmp.append(n.right.value)
                    node_lst.append(n.right)
            if node_lst[0]=="NONE" and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")
        for key,val in dict.items():
            for i in range(0,len(val)):
                itm=val[i]
                if itm==k and i<len(val)-1:
                    return val[i+1]
        return -1

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(2)
    tree.root.right=Node(6)
    tree.root.left.left=Node(8)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(5)
    print(tree.print_tree('preorder'))
    k=2
    print(tree.FindNextRightNodeBinaryTree(k))
    k = 4
    print(tree.FindNextRightNodeBinaryTree(k))


if __name__=='__main__':
    main()