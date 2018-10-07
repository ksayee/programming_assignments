'''
Difference between sums of odd level and even level nodes of a Binary Tree
Given a a Binary Tree, find the difference between the sum of nodes at odd level and the sum of nodes at even level. Consider root as level 1, left and right children of root as level 2 and so on.
For example, in the following tree, sum of nodes at odd level is (5 + 1 + 4 + 8) which is 18. And sum of nodes at even level is (2 + 6 + 3 + 7 + 9) which is 27. The output for following tree should be 18 – 27 which is -9.

      5
    /   \
   2     6
 /  \     \
1    4     8
    /     / \
   3     7   9
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
        if start==None:
            return
        tmp.append(str(start.value))
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def print_tree(self,traversal):
        if traversal=='preorder':
            start=self.root
            tmp=[]
            self.preorder(start,tmp)
        return '-'.join(tmp)

    def DiffBetweenOddAndEvenLevelsBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        height=1
        dict={}
        tmp=[]
        tmp.append(start.value)
        dict[height]=tmp

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    node_lst.append(n.left)
                    tmp.append(n.left.value)
                if n.right!=None:
                    node_lst.append(n.right)
                    tmp.append(n.right.value)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            dict[height]=tmp
            node_lst.pop(0)
            node_lst.append('NONE')

        odd_sum=0
        even_sum=0
        for key, val in dict.items():
            if key%2!=0:
                sum=0
                for l in val:
                    sum=sum+l
                odd_sum=odd_sum+sum
        
        for key, val in dict.items():
            if key%2==0:
                sum=0
                for l in val:
                    sum=sum+l
                even_sum=even_sum+sum

        return odd_sum-even_sum
def main():

    tree=BinaryTree(5)
    tree.root.left=Node(2)
    tree.root.right=Node(6)
    tree.root.left.left=Node(1)
    tree.root.left.right = Node(4)
    tree.root.left.right.left = Node(3)
    tree.root.right.right = Node(8)
    tree.root.right.right.left = Node(7)
    tree.root.right.right.right = Node(9)
    print(tree.print_tree('preorder'))
    print(tree.DiffBetweenOddAndEvenLevelsBinaryTree())

if __name__=='__main__':
    main()