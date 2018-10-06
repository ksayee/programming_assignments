'''
Given a binary tree, print out all of its root-to-leaf paths one per line.
Asked by Varun Bhatia

Here is the solution.

Algorithm:

initialize: pathlen = 0, path[1000]
/*1000 is some max limit for paths, it can change*/

/*printPathsRecur traverses nodes of tree in preorder */
printPathsRecur(tree, path[], pathlen)
   1) If node is not NULL then
         a) push data to path array:
                path[pathlen] = node->data.
         b) increment pathlen
                pathlen++
   2) If node is a leaf node then print the path array.
   3) Else
        a) Call printPathsRecur for left subtree
                 printPathsRecur(node->left, path, pathLen)
        b) Call printPathsRecur for right subtree.
                printPathsRecur(node->right, path, pathLen)
Example:
Example Tree
Example Tree

Output for the above example will be

  1 2 4
  1 2 5
  1 3
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

    def PrintRootToLeafPathBinaryTree(self):

        start=self.root
        tmp=[]
        self.PrintRootToLeafPath(start,tmp)

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print(tree.print_tree('preorder'))
    tree.PrintRootToLeafPathBinaryTree()

if __name__=='__main__':
    main()