'''
965. Univalued Binary Tree
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.
Example 1:
Input: [1,1,1,1,1,null,1]
Output: true
Example 2:
Input: [2,2,2,5,2]
Output: false
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def CheckUnivaluedTree_recur(self,start,tmp):
        if start is None:
            return True
        tmp.append(start.value)
        if len(set(tmp))>1:
            return False
        left_flg=self.CheckUnivaluedTree_recur(start.left,tmp)
        right_flg=self.CheckUnivaluedTree_recur(start.right,tmp)
        if left_flg==False or right_flg==False:
            return False
        return True

    def CheckUnivaluedTree(self):
        start=self.root
        tmp=[]
        flg=self.CheckUnivaluedTree_recur(start,tmp)
        return flg

def main():
    
    tree=BinaryTree(1)
    tree.root.left=Node(1)
    tree.root.right=Node(1)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(1)
    tree.root.right.right = Node(1)
    print(tree.CheckUnivaluedTree())

    tree1 = BinaryTree(2)
    tree1.root.left = Node(2)
    tree1.root.right = Node(2)
    tree1.root.left.left = Node(5)
    tree1.root.left.right = Node(2)
    print(tree1.CheckUnivaluedTree())

if __name__=='__main__':
    main()