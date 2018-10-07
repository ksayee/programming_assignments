'''
Check if a Binary Tree (not BST) has duplicate values
Check if a Binary Tree (not BST) has duplicate values

Examples:

Input : Root of below tree
         1
       /   \
      2     3
             \
              2
Output : Yes
Explanation : The duplicate value is 2.

Input : Root of below tree
         1
       /   \
     20     3
             \
              4
Output : No
Explanation : There are no duplicates.
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

    def GetValues(self,start,tmp):

        if start is None:
            return
        tmp.append(start.value)
        self.GetValues(start.left,tmp)
        self.GetValues(start.right,tmp)

    def CheckDuplicateValuesBinaryTree(self):
        start=self.root
        tmp=[]
        self.GetValues(start,tmp)
        if len(tmp)==len(set(tmp)):
            return False
        else:
            return True

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.right.right = Node(2)
    print(tree.print_tree('preorder'))
    print(tree.CheckDuplicateValuesBinaryTree())

    tree1 = BinaryTree(1)
    tree1.root.left = Node(20)
    tree1.root.right = Node(3)
    tree1.root.right.right = Node(4)
    print(tree1.print_tree('preorder'))
    print(tree1.CheckDuplicateValuesBinaryTree())

if __name__=='__main__':
    main()