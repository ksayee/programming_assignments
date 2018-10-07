'''
Find maximum level sum in Binary Tree
Given a Binary Tree having positive and negative nodes, the task is to find maximum sum level in it.

Examples:

Input :               4
                    /   \
                   2    -5
                  / \    /\
                -1   3 -2  6
Output: 6
Explanation :
Sum of all nodes of 0'th level is 4
Sum of all nodes of 1'th level is -3
Sum of all nodes of 0'th level is 6
Hence maximum sum is 6

Input :          1
               /   \
             2      3
           /  \      \
          4    5      8
                    /   \
                   6     7
Output :  17
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

    def MaxLevelSumBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        height=1
        dict={}
        tmp=[]
        tmp.append(start.value)
        dict[height]=tmp

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
            node_lst.append('NONE')

        out_lst=[]

        for key,val in dict.items():
            sum=0
            for l in val:
                sum=sum+l
            out_lst.append(sum)
        return sorted(out_lst,reverse=True)[0]

def main():

    tree=BinaryTree(4)
    tree.root.left=Node(2)
    tree.root.right=Node(-5)
    tree.root.left.left=Node(-1)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(-2)
    tree.root.right.right = Node(6)
    print(tree.print_tree('preorder'))
    print(tree.MaxLevelSumBinaryTree())

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(5)
    tree1.root.right.right = Node(8)
    tree1.root.right.right.left = Node(6)
    tree1.root.right.right.right = Node(7)
    print(tree1.print_tree('preorder'))
    print(tree1.MaxLevelSumBinaryTree())

if __name__=='__main__':
    main()