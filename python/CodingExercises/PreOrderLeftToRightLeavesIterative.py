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

    def PreOrderLeftToRightLeavesIterative(self):

        start=self.root
        num_lst=[]
        node_lst=[]
        node_lst.append(start)
        while len(node_lst)>0:

            n=node_lst[-1]
            node_lst.pop()
            if n.left is None and n.right is None:
                num_lst.append(n.value)

            if n.right!=None:
                node_lst.append(n.right)
            if n.left!=None:
                node_lst.append(n.left)
        return num_lst

def main():

    tree1=BinaryTree(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)
    tree1.root.left.left=Node(11)
    tree1.root.left.right=Node(4)
    tree1.root.right.left=Node(6)
    tree1.root.right.right=Node(7)
    tree1.root.left.left.left = Node(12)
    print(tree1.print_tree('preorder'))
    print(tree1.PreOrderLeftToRightLeavesIterative())

if __name__=='__main__':
    main()