'''
Print a Binary Tree in Vertical Order | Set 3 (Using Level Order Traversal)
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.


           1
         /   \
       2       3
     /  \     /  \
   4     5   6    7
              \    \
               8    9

The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9
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

    def PrintVerticalOrderBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        dict[start.value]=0
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[0]=tmp

        while len(node_lst)!=0:
            n=node_lst[-1]
            node_lst.pop()
            if n.left!=None:
                val=dict[n.value]
                if (val-1) in fnl_dict.keys():
                    fnl_dict[val-1].append(n.left.value)
                else:
                    tmp=[]
                    tmp.append(n.left.value)
                    fnl_dict[val-1]=tmp
                dict[n.left.value]=val-1
            if n.right!=None:
                val=dict[n.value]
                if (val+1) in fnl_dict.keys():
                    fnl_dict[val+1].append(n.right.value)
                else:
                    tmp=[]
                    tmp.append(n.right.value)
                    fnl_dict[val+1]=tmp
                dict[n.right.value]=val+1

            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)

        sort_lst=sorted(fnl_dict.items(),key=lambda x:x[0])
        for key in sort_lst:
            print(key[1])

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left= Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.left.right = Node(8)
    tree.root.right.right.right = Node(9)
    print(tree.print_tree('preorder'))
    tree.PrintVerticalOrderBinaryTree()

if __name__=='__main__':
    main()