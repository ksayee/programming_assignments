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
        stk1=[]
        stk2=[]
        stk1.append(start)

        while len(stk1)!=0:
            n=stk1[-1]
            stk1.pop()
            stk2.append(n)
            for i in range(0,len(n.child)):
                stk1.append(n.child[i])
        tmp=[]
        while len(stk2)!=0:
            n=stk2[-1]
            stk2.pop()
            tmp.append(n.value)
        return tmp

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