# Sum of all elements in a binary tree

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

    def GetLeaves(self,start,tmp):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
        self.GetLeaves(start.left,tmp)
        self.GetLeaves(start.right,tmp)

    def LeafTraversal2BinaryTreeSame(self):

        tmp=[]
        self.GetLeaves(self.root,tmp)
        return tmp

    def CheckList(self,lst1,lst2):

        flg=True
        if len(lst1)!=len(lst2):
            flg=False
            return flg
        else:
            while len(lst1)>0:
                if lst1.pop()==lst2.pop():
                    continue
                else:
                    flg=False
                    break

        return flg

def main():

    tree1=BinaryTree(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)
    tree1.root.left.right=Node(4)
    tree1.root.right.left=Node(6)
    tree1.root.right.right=Node(7)

    tree2 = BinaryTree(0)
    tree2.root.left = Node(5)
    tree2.root.right = Node(8)
    tree2.root.left.right = Node(4)
    tree2.root.right.left = Node(6)
    tree2.root.right.right = Node(7)

    print(tree1.print_tree('preorder'))
    print(tree2.print_tree('preorder'))

    lst1=tree1.LeafTraversal2BinaryTreeSame()
    lst2=tree2.LeafTraversal2BinaryTreeSame()

    print(tree1.CheckList(lst1,lst2))

if __name__=='__main__':
    main()