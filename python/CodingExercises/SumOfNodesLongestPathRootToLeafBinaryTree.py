'''
Sum of nodes on the longest path from root to leaf node
Given a binary tree containing n nodes. The problem is to find the sum of all nodes on the longest path from root to leaf node. If two or more paths compete for the longest path, then the path having maximum sum of nodes is being considered.

Examples:

Input : Binary tree:
        4
       / \
      2   5
     / \ / \
    7  1 2  3
      /
     6
Output : 13

        4
       / \
      2   5
     / \ / \
    7  1 2  3
      /
     6

The highlighted nodes (4, 2, 1, 6) above are
part of the longest root to leaf path having
sum = (4 + 2 + 1 + 6) = 13
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

        if start is None:
            return
        tmp.append(str(start.value))
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def print_tree(self,traversal_type):
        start=self.root
        tmp=[]
        if traversal_type=='preorder':
            self.preorder(start,tmp)
            return '-'.join(tmp)

    def GetSumRootToLeaf(self,start,tmp,fnl_lst):

        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
            sum=0
            for l in tmp:
                sum=sum+l
            tup=(tmp.copy(),sum)
            fnl_lst.append(tup)
            tmp.pop()
        tmp.append(start.value)
        self.GetSumRootToLeaf(start.left,tmp,fnl_lst)
        self.GetSumRootToLeaf(start.right,tmp,fnl_lst)
        tmp.pop()


    def SumOfNodesLongestPathRootToLeafBinaryTree(self):

        start=self.root
        tmp=[]
        fnl_lst=[]
        self.GetSumRootToLeaf(start,tmp,fnl_lst)

        sort_lst=sorted(fnl_lst,key=lambda x:len(x[0]),reverse=True)

        return sort_lst[0][1]

def main():

    tree1=BinaryTree(4)
    tree1.root.left=Node(2)
    tree1.root.right=Node(5)
    tree1.root.left.left=Node(7)
    tree1.root.left.right=Node(1)
    tree1.root.right.left=Node(2)
    tree1.root.right.right=Node(3)
    tree1.root.left.right.left = Node(6)
    print(tree1.print_tree('preorder'))
    print(tree1.SumOfNodesLongestPathRootToLeafBinaryTree())

if __name__=='__main__':
    main()