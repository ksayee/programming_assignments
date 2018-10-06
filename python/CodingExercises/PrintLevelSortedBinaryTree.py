'''
Print Binary Tree levels in sorted order | Set 2 (Using set)
Given a tree, print the level order traversal in sorted order.

Examples :

Input :     7
          /    \
        6       5
       / \     / \
      4  3    2   1
Output :
7
5 6
1 2 3 4

Input :     7
          /    \
        16       1
       / \
      4   13
Output :
7
1 16
4 13
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

    def PrintLevelSortedBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        height=0
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
                    tmp.append(n.left.value)
                    node_lst.append(n.left)
                if n.right!=None:
                    tmp.append(n.right.value)
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            node_lst.pop(0)
            dict[height]=list(sorted(tmp))
            node_lst.append('NONE')
        for key,val in dict.items():
            print(val)

def main():

    tree=BinaryTree(7)
    tree.root.left=Node(6)
    tree.root.right = Node(5)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(2)
    tree.root.right.right = Node(1)
    print(tree.print_tree('preorder'))
    tree.PrintLevelSortedBinaryTree()

    tree1 = BinaryTree(7)
    tree1.root.left = Node(16)
    tree1.root.right = Node(1)
    tree1.root.left.left = Node(4)
    tree1.root.left.right = Node(13)
    print(tree1.print_tree('preorder'))
    tree1.PrintLevelSortedBinaryTree()

if __name__=='__main__':
    main()