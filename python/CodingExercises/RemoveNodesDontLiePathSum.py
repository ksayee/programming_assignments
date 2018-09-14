# Remove all nodes which don’t lie in any path with sum>= k
# Given a binary tree, a complete path is defined as a path from root to a leaf.
# The sum of all nodes on that path is defined as the sum of that path. Given a number K, you have to remove (prune the tree)
# all nodes which don’t lie in any path with sum>=k.
# Note: A node can be part of multiple paths. So we have to delete it only in case when all paths from it have sum less than K.

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.visited=False


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

    def CheckSum(self,start,sum,k):

        if start is None:
            return
        sum=sum+start.value
        start.left=self.CheckSum(start.left,sum,k)
        start.right=self.CheckSum(start.right, sum,k)

        if start.left is None and start.right is None:
            if sum<k:
                start=None
        return start

    def RemoveNodesDontLiePathSum(self,k):

        n=self.CheckSum(self.root,0,k)
        return

    def RemoveNodesDontLiePathSumIterative(self, k):

        node_lst=[]

        node_lst.append(self.root)
        sum=self.root.value


        while len(node_lst)!=0:

            parent=node_lst[-1]
            child=parent.left

            while child.left!=None:
                node_lst.append(child)
                sum = sum + child.value
                parent=child
                child=child.left
            sum=sum+child.value

            if sum<k:
                if child.left is None and child.right is None:
                    parent.left=None
                    sum=sum-child.value
                else:
                    node_lst.append(child)

            parent = node_lst[-1]
            child = parent.right

            while child.right != None:
                node_lst.append(child)
                sum = sum + child.value
                parent = child
                child = child.right
                sum = sum + child.value
            if sum < k:
                if child.left is None and child.right is None:
                    parent.right = None
                    sum = sum - child.value
                else:
                    node_lst.append(child)



def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.left.left.left = Node(8)
    tree.root.left.left.right = Node(9)
    tree.root.left.right.left = Node(12)
    tree.root.left.left.right.left = Node(13)
    tree.root.left.left.right.right = Node(14)
    tree.root.left.left.right.right.left = Node(15)
    tree.root.right.left=Node(6)
    tree.root.right.right=Node(7)
    tree.root.right.right.left = Node(10)
    tree.root.right.right.left.right = Node(11)
    print(tree.print_tree('preorder'))
    k=20
    print(tree.RemoveNodesDontLiePathSum(k))
    print(tree.print_tree('preorder'))

if __name__=='__main__':
    main()