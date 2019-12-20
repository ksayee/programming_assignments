'''
Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.
For example, given k = 18 and the following binary tree:
    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def PreOrderTraversal(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.value))
        self.PreOrderTraversal(start.left,tmp)
        self.PreOrderTraversal(start.right,tmp)

    def DisplayTree(self):
        start=self.root
        tmp=[]
        self.PreOrderTraversal(start,tmp)
        return '-'.join(tmp)

    def FindPathSum_recur(self,start,tmp,path_list,k):
        if start is None:
            return
        if start.left is None and start.right is None:
            tmp.append(start.value)
            sum=0
            for value in tmp:
                sum=sum+value
            if sum==k:
                path_list.append(tmp.copy())
            tmp.pop()
            return
        tmp.append(start.value)
        self.FindPathSum_recur(start.left,tmp,path_list,k)
        self.FindPathSum_recur(start.right,tmp,path_list,k)
        tmp.pop()

    def FindPathSum(self,k):
        start=self.root
        tmp=[]
        path_list=[]
        self.FindPathSum_recur(start,tmp,path_list,k)
        return path_list

def main():

    tree=BinaryTree(8)
    tree.root.left=Node(4)
    tree.root.right = Node(13)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(19)
    print(tree.DisplayTree())
    k=18
    print(tree.FindPathSum(k))

if __name__=='__main__':
    main()