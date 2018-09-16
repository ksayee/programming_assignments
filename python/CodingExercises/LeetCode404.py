'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

class LeetCode404Node(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class LeetCode404BinaryTree(object):

    def __init__(self,root):
        self.root=LeetCode404Node(root)

    def preorder(self,start,traversal):
        if start!=None:
            traversal=self.preorder(start.left,traversal)
            traversal=traversal+str(start.val)+'-'
            traversal = self.preorder(start.right, traversal)
        return traversal

    def print_tree(self,traversal):

        if traversal=='preorder':
            return self.preorder(self.root,'')

    def CalculateSum(self,start,tmp):

        if start is None:
            return
        if start.left!=None and (start.left.left is None and start.left.right is None):
            tmp.append(start.left.val)
        self.CalculateSum(start.left,tmp)
        self.CalculateSum(start.right,tmp)

    def LeftLeavesBinaryTree(self):

        tmp=[]
        self.CalculateSum(self.root,tmp)

        sum=0
        for l in tmp:
            sum=sum+l
        return sum

    def LeftLeavesBinaryTreeIterative(self):

        node_lst=[]
        val_lst=[]

        node_lst.append(self.root)

        while len(node_lst)!=0:

            n=node_lst[-1]
            node_lst.pop()
            if n.left!=None and (n.left.left is None and n.left.right is None):
                val_lst.append(n.left.val)

            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)
        sum=0
        for l in val_lst:
            sum=sum+l

        return sum

def main():

    tree = LeetCode404BinaryTree(1)
    tree.root.left = LeetCode404Node(2)
    tree.root.right = LeetCode404Node(3)
    tree.root.left.left = LeetCode404Node(4)
    tree.root.left.right = LeetCode404Node(5)
    tree.root.right.left = LeetCode404Node(6)
    tree.root.right.right = LeetCode404Node(7)
    tree.root.left.left.left = LeetCode404Node(8)
    tree.root.left.left.right = LeetCode404Node(9)
    tree.root.left.right.left = LeetCode404Node(10)
    tree.root.left.right.right = LeetCode404Node(11)
    tree.root.right.left.left = LeetCode404Node(12)
    tree.root.right.left.right = LeetCode404Node(13)
    tree.root.right.right.left = LeetCode404Node(14)
    tree.root.right.right.right = LeetCode404Node(15)

    print(tree.print_tree('preorder'))
    print(tree.LeftLeavesBinaryTree())
    print(tree.LeftLeavesBinaryTreeIterative())

    tree = LeetCode404BinaryTree(3)
    tree.root.left = LeetCode404Node(9)
    tree.root.right = LeetCode404Node(20)
    tree.root.right.left = LeetCode404Node(15)
    tree.root.right.right = LeetCode404Node(7)

    print(tree.print_tree('preorder'))
    print(tree.LeftLeavesBinaryTree())
    print(tree.LeftLeavesBinaryTreeIterative())

if __name__=='__main__':
    main()