'''
Maximum width of a binary tree
Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of widths of all levels.
Let us consider the below example tree.

         1
        /  \
       2    3
     /  \     \
    4    5     8
              /  \
             6    7
For the above tree,
width of level 1 is 1,
width of level 2 is 2,
width of level 3 is 3
width of level 4 is 2.

So the maximum width of the tree is 3.
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

    def MaximumWidthBinaryTree(self):

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

                if n.left!=None:
                    tmp.append(n.left.value)
                    node_lst.append(n.left)
                if n.right!=None:
                    tmp.append(n.right.value)
                    node_lst.append(n.right)
            if node_lst[0]=="NONE" and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append("NONE")

        out_lst=[]
        for key,val in dict.items():
            out_lst.append(len(val))

        return sorted(out_lst,reverse=True)[0]
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(8)
    tree.root.right.right.left = Node(6)
    tree.root.right.right.right = Node(7)
    print(tree.print_tree('preorder'))
    print(tree.MaximumWidthBinaryTree())

if __name__=='__main__':
    main()