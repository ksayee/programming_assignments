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

    def LevelOrderTraversalBinaryTree(self):

        start=self.root

        tmp=[]

        tmp.append(start)
        fnl_lst=[]

        while len(tmp)!=0:
            node=tmp.pop(0)
            fnl_lst.append(node.value)

            if node.left!=None:
                tmp.append(node.left)
            if node.right!=None:
                tmp.append(node.right)

        return ' '.join(fnl_lst)

    def LevelOrderTraversalLevelByLevelBinaryTree(self):

        start=self.root

        tmp=[]
        tmp.append(start)
        tmp.append('None')
        fnl_lst=[]
        while len(tmp)!=0:
            while tmp[0]!='None':
                node=tmp.pop(0)
                fnl_lst.append(node.value)
                if node.left!=None:
                    tmp.append(node.left)
                if node.right!=None:
                    tmp.append(node.right)
            if tmp[0]=='None' and len(tmp)==1:
                break
            else:
                tmp.pop(0)
                fnl_lst.append('\n')
                tmp.append('None')
        return ''.join(fnl_lst)

def main():

    tree=BinaryTree('a')
    tree.root.left=Node('b')
    tree.root.right=Node('c')
    tree.root.left.left=Node('d')
    tree.root.left.right=Node('e')
    tree.root.right.left=Node('f')
    tree.root.right.right=Node('g')
    tree.root.left.left.left = Node('h')
    tree.root.left.left.right = Node('i')
    tree.root.right.left.left = Node('j')
    tree.root.right.left.right= Node('k')
    tree.root.right.right.right= Node('l')
    print(tree.print_tree('preorder'))
    print(tree.LevelOrderTraversalBinaryTree())
    print(tree.LevelOrderTraversalLevelByLevelBinaryTree())

if __name__=='__main__':
    main()