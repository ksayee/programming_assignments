# Construct a Binary Tree in Python.

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
        if traversal_type=='preorder':
            tmp=[]
            start=self.root
            self.preorder(start,tmp)
            return ' '.join(tmp)
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def MaxSumTree_recur(self,start,tmp,curr_sum):

        if start is None:
            return
        curr_sum=curr_sum+start.value

        if start.left is None and start.right is None:
            tup=(start,curr_sum)
            tmp.append(tup)
        self.MaxSumTree_recur(start.left, tmp, curr_sum)
        self.MaxSumTree_recur(start.right, tmp, curr_sum)

    def PrintPath(self,start,leaf_node):

        if start is None:
            return False
        if start ==leaf_node or self.PrintPath(start.left,leaf_node)==True or self.PrintPath(start.right,leaf_node)==True :
            print(start.value,end=' ')
            return True
        return False


    def MaxSumLeafBinaryTree(self):

        start=self.root
        tmp=[]
        curr_sum=0
        leaf_node=''
        self.MaxSumTree_recur(start,tmp,curr_sum)
        start = self.root
        print("Maximum Sum:",sorted(tmp,key=lambda x:x[1],reverse=True)[0][1])
        self.PrintPath(start,sorted(tmp,key=lambda x:x[1],reverse=True)[0][0])

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(-2)
    tree.root.right=Node(7)
    tree.root.left.left=Node(8)
    tree.root.left.right=Node(-4)
    print(tree.print_tree('preorder'))
    tree.MaxSumLeafBinaryTree()

if __name__=='__main__':
    main()