'''
Right view of Binary Tree using Queue
Given a Binary Tree, print Right view of it. Right view of a Binary Tree is set of nodes visible when tree is visited from Right side.

Examples:

Input :
              10
            /     \
          2         3
        /   \    /    \
       7     8  12     15
                      /
                    14
Output : 10 3 15 14
The output nodes are the rightmost
nodes of their respective levels.
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

    def PrintRightViewBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        height=0
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[height]=tmp

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
            height = height + 1
            fnl_dict[height] = tmp
            node_lst.pop(0)
            node_lst.append('NONE')

        sort_lst=sorted(fnl_dict.items(),key=lambda x:x[0])
        for key in sort_lst:
            lst=key[1]
            print(key[1][-1],end=' ')

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(7)
    tree.root.left.right = Node(8)
    tree.root.right.left= Node(12)
    tree.root.right.right = Node(15)
    tree.root.right.right.left = Node(14)
    print(tree.print_tree('preorder'))
    tree.PrintRightViewBinaryTree()

if __name__=='__main__':
    main()