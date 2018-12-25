# Check if a given tree is a binary Search tree in recursive and iterative both.

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
        tmp.append(start.value)
        self.preorder(start.left,tmp)
        self.preorder(start.right,tmp)

    def PrintTraversal(self,traversaltype):
        tmp=[]
        start=self.root
        if traversaltype=='Preorder':
            self.preorder(start,tmp)
        return tmp

    def CheckBST_recur(self,start,tmp):
        if start is None:
            return

        if start.left!=None and start.right!=None:
            if start.left.value<start.value and start.right.value>start.value:
                tmp.append(True)
            else:
                tmp.append(False)
        elif start.left==None and start.right!=None:
            if start.right.value>start.value:
                tmp.append(True)
            else:
                tmp.append(False)
        elif start.left!= None and start.right == None:
            if start.left.value < start.value:
                tmp.append(True)
            else:
                tmp.append(False)
        self.CheckBST_recur(start.left, tmp)
        self.CheckBST_recur(start.right, tmp)

    def CheckBST_iterative(self,start, tmp):
        node_lst=[]
        node_lst.append(start)
        while len(node_lst)!=0:
            n=node_lst[0]
            node_lst.pop(0)
            if n.left!=None and n.right!=None:
                if n.left.value<n.value and n.right.value>n.value:
                    tmp.append(True)
                else:
                    tmp.append(False)
            elif n.left != None and n.right==None:
                if n.left.value < n.value:
                    tmp.append(True)
                else:
                    tmp.append(False)
            elif n.left == None and n.right != None:
                if n.right.value > n.value:
                    tmp.append(True)
                else:
                    tmp.append(False)
            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)
        return tmp

    def CheckBST_R(self):
        tmp=[]
        start=self.root
        self.CheckBST_recur(start,tmp)
        return tmp

    def CheckBST_ITR(self):
        tmp=[]
        start=self.root
        self.CheckBST_iterative(start, tmp)
        return tmp

def main():

    tree=BinaryTree(10)
    tree.root.left=Node(5)
    tree.root.right=Node(40)
    tree.root.left.left=Node(1)
    tree.root.left.right=Node(7)
    tree.root.right.right=Node(50)
    print(tree.PrintTraversal('Preorder'))
    print(tree.CheckBST_R())
    print(tree.CheckBST_ITR())

if __name__=='__main__':
    main()