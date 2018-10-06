'''
Print Nodes in Top View of Binary Tree
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
Given a binary tree, print the top view of it. The output nodes can be printed in any order. Expected time complexity is O(n)
A node x is there in output if x is the topmost node at its horizontal distance.
Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
Top view of the above binary tree is
4 2 1 3 7

        1
      /   \
    2       3
      \
        4
          \
            5
             \
               6
Top view of the above binary tree is
2 1 3 6
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

    def PrintRootToLeafPath(self,start,tmp):

        if start.left is None and start.right is None:
            tmp.append(str(start.value))
            print('-'.join(tmp))
            return
        tmp.append(str(start.value))
        self.PrintRootToLeafPath(start.left,tmp)
        tmp.pop()
        self.PrintRootToLeafPath(start.right,tmp)
        tmp.pop()

    def PrintTopViewBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[0]=tmp
        dict[start.value]=0

        while len(node_lst)!=0:
            n=node_lst[0]
            node_lst.pop(0)
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
        top_lst=[]
        for key in sort_lst:
            top_lst.append(key[1][0])
        return top_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.print_tree('preorder'))
    print(tree.PrintTopViewBinaryTree())

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)
    tree1.root.left.right = Node(4)
    tree1.root.left.right.right = Node(5)
    tree1.root.left.right.right.right= Node(6)
    print(tree1.print_tree('preorder'))
    print(tree1.PrintTopViewBinaryTree())

if __name__=='__main__':
    main()