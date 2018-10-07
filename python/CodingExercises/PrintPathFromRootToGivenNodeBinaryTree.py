'''
Print path from root to a given node in a binary tree
Given a binary tree with distinct nodes(no two nodes have the same have data values). The problem is to print the path from root to a given node x. If node x is not present then print “No Path”.

Examples:

Input :          1
               /   \
              2     3
             / \   /  \
            4   5  6   7

               x = 5

Output : 1->2->5
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,traversal):
        if start!=None:
            traversal=traversal+ (str(start.value)+ '-')
            traversal=self.preorder(start.left,traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(self.root,'')
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def PathRootToGivenNode(self,start,tmp,k):

        if start.left is None and start.right is None:
            tmp.append(str(start.value))
            if start.value==k:
                print('-'.join(tmp))
            return
        if start.value==k:
            tmp.append(str(start.value))
            print('-'.join(tmp))
            tmp.pop()
        tmp.append(str(start.value))
        self.PathRootToGivenNode(start.left,tmp,k)
        tmp.pop()
        self.PathRootToGivenNode(start.right,tmp,k)
        tmp.pop()

    def PrintPathFromRootToGivenNodeBinaryTree(self,k):

        start=self.root
        tmp=[]
        self.PathRootToGivenNode(start,tmp,k)


    
def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.print_tree('preorder'))
    k=5
    tree.PrintPathFromRootToGivenNodeBinaryTree(k)

if __name__=='__main__':
    main()