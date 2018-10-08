'''
429. N-ary Tree Level Order Traversal
DescriptionHintsSubmissionsDiscussSolution
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example, given a 3-ary tree:
We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]
'''

class Node(object):

    def __init__(self,value):
        self.value=value
        self.child=[]

class BinaryTree(object):

    def __init__(self,root):
        self.root=Node(root)

    def LeetCode429(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=1
        tmp=[]
        tmp.append(start.value)
        dict={}
        dict[height]=tmp
        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                for chd in n.child:
                    tmp.append(chd.value)
                    node_lst.append(chd)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")
        return dict

def main():

    tree=BinaryTree(1)
    tree.root.child.append(Node(3))
    tree.root.child.append(Node(2))
    tree.root.child.append(Node(4))
    tree.root.child[0].child.append(Node(5))
    tree.root.child[0].child.append(Node(6))
    print(tree.LeetCode429())

if __name__=='__main__':
    main()