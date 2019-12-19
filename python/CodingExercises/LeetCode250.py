'''
250. Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.
Example :
Input:  root = [5,1,5,5,5,null,5]
              5
             / \
            1   5
           / \   \
          5   5   5
Output: 4
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def CountUnivaluedSubtrees_recur(self,start,tmp):
        if start is None:
            return True
        left_flg=self.CountUnivaluedSubtrees_recur(start.left,tmp)
        right_flg=self.CountUnivaluedSubtrees_recur(start.right,tmp)
        if left_flg==False or right_flg==False:
            return False
        if start.left!=None and start.value!=start.left.value:
            return False
        if start.right!=None and start.value!=start.right.value:
            return False
        tmp.append(1)
        return True

    def CountUnivaluedSubtrees(self):
        start=self.root
        tmp=[]
        self.CountUnivaluedSubtrees_recur(start,tmp)
        return tmp

def main():
    
    tree=BinaryTree(5)
    tree.root.left=Node(1)
    tree.root.right=Node(5)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(5)
    tree.root.right.right = Node(5)
    print(tree.CountUnivaluedSubtrees())

if __name__=='__main__':
    main()