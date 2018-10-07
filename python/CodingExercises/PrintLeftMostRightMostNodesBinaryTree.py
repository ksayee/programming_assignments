'''
Print leftmost and rightmost nodes of a Binary Tree
Given a Binary Tree, Print the corner nodes at each level. The node at the leftmost and the node at the rightmost.
For example, output for following is 15, 10, 20, 8, 25.
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
A Simple Solution is to do two traversals using the approaches discussed for printing left view and right view.
Can we print all corner nodes using one traversal?
The idea is to use Level Order Traversal. To find first node, we use a variable isFirst.
To separate levels, we enqueue NULL after every level. So in level order traversal, if we see a NULL, we know next node would be first node of its level and therefore we set isFirst.
A special case to consider is, a tree like below.

   1
    \
     2
      \
       3
The output for above tree should be 1, 2, 3. We need make sure that the levels having only one node are handled and the node is printed only once. For this purpose, we maintain a separate variable isOne.
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

    def PrintLeftMostRightMostNodesBinaryTree(self):

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
            if len(lst)==1:
                print(lst[0],end=' ')
            else:
                print(lst[0],end=' ')
                print(lst[-1],end=' ')

def main():

    tree=BinaryTree(15)
    tree.root.left=Node(10)
    tree.root.right = Node(20)
    tree.root.left.left = Node(8)
    tree.root.left.right = Node(12)
    tree.root.right.left= Node(16)
    tree.root.right.right = Node(25)
    print(tree.print_tree('preorder'))
    tree.PrintLeftMostRightMostNodesBinaryTree()

    print('\n')
    tree1 = BinaryTree(1)
    tree1.root.right = Node(2)
    tree1.root.right.right = Node(3)
    print(tree1.print_tree('preorder'))
    tree1.PrintLeftMostRightMostNodesBinaryTree()
    
if __name__=='__main__':
    main()