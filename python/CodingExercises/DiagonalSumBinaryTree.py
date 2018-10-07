'''
Diagonal Sum of a Binary Tree
Consider lines of slope -1 passing between nodes (dotted lines in below diagram). Diagonal sum in a binary tree is sum of all node’s data lying between these lines. Given a Binary Tree, print all diagonal sums.

For the following input tree, output should be 9, 19, 42.
9 is sum of 1, 3 and 5.
19 is sum of 2, 6, 4 and 7.
42 is sum of 9, 10, 11 and 12.
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

    def DiagonalSumBinaryTree(self):

        start=self.root
        node_lst=[]
        diag=0
        node_lst.append(start)
        dict={}
        dict[start.value]=diag
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[diag]=tmp

        while len(node_lst)!=0:

            n=node_lst[-1]
            node_lst.pop()

            if n.left!=None:
                val=dict[n.value]
                if val+1 in fnl_dict.keys():
                    fnl_dict[val+1].append(n.left.value)
                else:
                    tmp=[]
                    tmp.append(n.left.value)
                    fnl_dict[val+1]=tmp
                dict[n.left.value]=val+1

            if n.right!=None:
                val=dict[n.value]
                if val in fnl_dict.keys():
                    fnl_dict[val].append(n.right.value)
                else:
                    tmp=[]
                    tmp.append(n.right.value)
                    fnl_dict[val]=tmp
                dict[n.right.value]=val
            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)

        out_lst=[]

        for key,val in fnl_dict.items():
            sum=0
            for l in val:
                sum=sum+l
            out_lst.append(sum)
        return out_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(9)
    tree.root.left.right = Node(6)
    tree.root.left.left.right = Node(10)
    tree.root.left.right.left = Node(11)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.left.left= Node(12)
    tree.root.right.left.right = Node(7)
    print(tree.print_tree('preorder'))
    print(tree.DiagonalSumBinaryTree())

if __name__=='__main__':
    main()