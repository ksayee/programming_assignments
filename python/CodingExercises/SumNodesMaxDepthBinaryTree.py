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

    def GetHeightBinaryTree(self,start):

        tmp=[]
        tmp.append(start)
        tmp.append('None')
        height=1
        while len(tmp)!=0:
            while tmp[0]!='None':
                node=tmp.pop(0)
                if node.left !=None:
                    tmp.append(node.left)
                if node.right!=None:
                    tmp.append(node.right)

            if tmp[0]=='None' and len(tmp)==1:
                break
            else:
                tmp.pop(0)
                tmp.append('None')
                height=height+1
        return height

    def GetSumMaxHeight(self,start,height):

        if start is None:
            return 0
        if height==1:
            return start.value
        return self.GetSumMaxHeight(start.left,height-1)+self.GetSumMaxHeight(start.right,height-1)

    def SumNodesMaxDepthBinaryTree(self):

        start=self.root
        height=self.GetHeightBinaryTree(start)
        sum=self.GetSumMaxHeight(start,height)

        return sum


def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.print_tree('preorder'))
    print(tree.SumNodesMaxDepthBinaryTree())

if __name__=='__main__':
    main()