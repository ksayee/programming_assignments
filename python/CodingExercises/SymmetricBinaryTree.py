'''
Check for Symmetric Binary Tree (Iterative Approach)
Given a binary tree, check whether it is a mirror of itself without recursion.
Examples:
Input :
     1
   /   \
  2     2
 / \   / \
3   4 4   3
Output : Symmetric
Input :
    1
   / \
  2   2
   \   \
   3    3
Output : Not Symmetric
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

    def SymmetricBinaryTree(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        flg=True
        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                node=node_lst[0]
                node_lst.pop(0)
                if node.left!=None:
                    tmp.append(node.left.data)
                else:
                    tmp.append(None)
                if node.right!=None:
                    tmp.append(node.right.data)
                else:
                    tmp.append(None)
                if node.left!=None:
                    node_lst.append(node.left)
                if node.right!=None:
                    node_lst.append(node.right)
            if node_lst[0]=="NONE" and len(node_lst)==1:
                break
            if tmp!=list(reversed(tmp)):
                flg=False
                break
            node_lst.append("NONE")
            node_lst.pop(0)
        return flg

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(3)
    print(tree.SymmetricBinaryTree())

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(2)
    tree.root.left.right = Node(3)
    tree.root.left.right = Node(4)
    tree.root.right.right = Node(3)
    print(tree.SymmetricBinaryTree())

if __name__=='__main__':
    main()