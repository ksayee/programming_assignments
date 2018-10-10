'''
Given an n-ary tree, return the preorder traversal of its nodes' values.
For example, given a 3-ary tree:
Return its preorder traversal as: [1,3,5,6,2,4].
'''

class Node(object):

    def __init__(self,value):
        self.value=value
        self.child=[]

class BinaryTree(object):

    def __init__(self,root):
        self.root=Node(root)

    def LeetCode589(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        tmp=[]
        while len(node_lst)!=0:
            n=node_lst[-1]
            node_lst.pop()
            tmp.append(n.value)
            for i in range(len(n.child)-1,-1,-1):
                node_lst.append(n.child[i])
        print(tmp)

def main():

    tree=BinaryTree(1)
    tree.root.child.append(Node(3))
    tree.root.child.append(Node(2))
    tree.root.child.append(Node(4))
    tree.root.child[0].child.append(Node(5))
    tree.root.child[0].child.append(Node(6))
    print(tree.LeetCode589())

if __name__=='__main__':
    main()