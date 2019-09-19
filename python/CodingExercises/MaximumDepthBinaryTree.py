'''
Write a Program to Find the Maximum Depth or Height of a Tree
Given a binary tree, find height of it. Height of empty tree is 0 and height of below tree is 3.
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def MaximumDepthBinaryTree(self):
        start=self.root
        dict={}
        node_lst=[]
        node_lst.append(start)
        height=1
        dict[height]=node_lst.copy()
        node_lst.append("NONE")

        while len(node_lst)!=0:
            while node_lst[0]!="NONE":
                node=node_lst[0]
                node_lst.pop(0)
                if node.left!=None:
                    node_lst.append(node.left)
                if node.right!=None:
                    node_lst.append(node.right)
            if node_lst[0]=="NONE" and len(node_lst)==1:
                break
            node_lst.pop(0)
            height=height+1
            dict[height]=node_lst.copy()
            node_lst.append("NONE")
        return sorted(dict.keys(),reverse=True)[0]
def main():

    tree=BinaryTree(6)
    tree.root.left=Node(5)
    tree.root.right = Node(4)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(2)
    tree.root.right.right = Node(5)
    print(tree.MaximumDepthBinaryTree())

if __name__=='__main__':
    main()