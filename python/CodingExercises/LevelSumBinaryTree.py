# Level sum of each level in a binary tree.

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


    def LevelSumBinaryTree(self):

        node_lst=[]
        sum_lst=[]
        start=self.root

        node_lst.append(start)
        sum_lst.append(start.value)

        while len(node_lst)>0:

            tmp=[]
            sum=0

            while len(node_lst)>0:
                n=node_lst[-1]
                if n.left!=None:
                    tmp.append(n.left)
                if n.right!=None:
                    tmp.append(n.right)
                node_lst.pop()

            if len(tmp)>0:
                for itm in tmp:
                    sum = sum + itm.value
                sum_lst.append(sum)
                node_lst=tmp

        return sum_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    tree.root.left.left.left=Node(8)
    tree.root.left.left.right = Node(9)
    tree.root.left.right.left = Node(10)
    tree.root.left.right.right = Node(11)
    tree.root.right.left.left = Node(12)
    tree.root.right.left.right = Node(13)
    tree.root.right.right.left = Node(14)
    tree.root.right.right.right = Node(15)
    print(tree.print_tree('preorder'))
    print(tree.print_tree('inorder'))
    print(tree.print_tree('postorder'))
    print(tree.LevelSumBinaryTree())

if __name__=='__main__':
    main()