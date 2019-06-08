'''
This problem was asked by Morgan Stanley.
In Ancient Greece, it was common to
write text with the first line going left to right,
the second line going right to left, and continuing to go back and forth.
This style was called "boustrophedon".
Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrder(self,tmp,start):
        if start is None:
            return
        tmp.append(start.value)
        self.PreOrder(tmp,start.left)
        self.PreOrder(tmp,start.right)


    def DailyCodingProblem258(self):
        start=self.root
        tmp=[]
        self.PreOrder(tmp,start)
        print("Printing Tree in PreOrder")
        for val in tmp:
            print(val,end=" ")
        print()
        tmp=[]
        fnl_lst=[]
        self.Boustrophedon(tmp,start,fnl_lst)
        print("Printing Tree in boustrophedon")
        for val in fnl_lst:
            print(val,end=" ")

    def Boustrophedon(self,tmp,start,fnl_lst):
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")

        while len(node_lst)!=0:
            while node_lst[0]!="NONE":
                n=node_lst[0]
                tmp.append(n.value)
                node_lst.pop(0)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                tmp.append('BREAK')
                break
            tmp.append('BREAK')
            node_lst.pop(0)
            node_lst.append("NONE")

        i=0
        while len(tmp)!=0:
            lst=[]
            while tmp[0]!='BREAK':
                lst.append(tmp[0])
                tmp.pop(0)
            if i%2!=0:
                lst.reverse()
            i=i+1
            fnl_lst.extend(lst)
            if tmp[0]=='BREAK' and len(tmp)==1:
                break
            tmp.pop(0)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.DailyCodingProblem258()

if __name__=='__main__':
    main()