# Construct a Binary Tree in Python.

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

    def inorder(self,start,traversal):
        if start!=None:
            traversal = self.preorder(start.left, traversal)
            traversal=traversal+ (str(start.value)+ '-')
            traversal = self.preorder(start.right, traversal)
        return traversal

    def postorder(self,start,traversal):
        if start!=None:
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
            traversal = traversal + (str(start.value) + '-')
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(self.root,'')
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def CheckSumBinaryTree(self,start,tmp):

        if start is None:
            return
        if start.left!=None and start.right!=None:
            if start.value==start.left.value+start.right.value:
                tmp.append(True)
            else:
                tmp.append(False)
        if start.left != None and start.right is None:
            if start.value == start.left.value:
                tmp.append(True)
            else:
                tmp.append(False)
        if start.left is None and start.right != None:
            if start.value == start.right.value:
                tmp.append(True)
            else:
                tmp.append(False)
        self.CheckSumBinaryTree(start.left,tmp)
        self.CheckSumBinaryTree(start.right,tmp)


    def ChildrenSumBinaryTree(self):

        start=self.root
        tmp=[]
        self.CheckSumBinaryTree(start,tmp)
        for key in tmp:
            if key==False:
                return False
        return True

    def ChildrenSumBinaryTree_iterative(self):

        start=self.root

        node_lst=[]

        node_lst.append(start)
        flg=True

        while len(node_lst)!=0:

            n=node_lst.pop()

            if n.left!=None and n.right!=None:
                if n.value!=n.left.value+n.right.value:
                    flg=False
                    break

            if n.left != None and n.right is None:
                if n.value != n.left.value:
                    flg = False
                    break

            if n.left is None and n.right!=None:
                if n.value != n.right.value:
                    flg = False
                    break

            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)

        return flg

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(8)
    tree.root.right=Node(2)
    tree.root.left.left=Node(3)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(2)
    print(tree.print_tree('preorder'))
    print(tree.ChildrenSumBinaryTree())
    print(tree.ChildrenSumBinaryTree_iterative())

if __name__=='__main__':
    main()