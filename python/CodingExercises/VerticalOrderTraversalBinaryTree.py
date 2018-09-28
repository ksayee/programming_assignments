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

    def VerticalOrderTraversalBinaryTree(self):

        dict={}

        start=self.root
        tmp=[]
        tmp.append(start)
        dict[start.value]=0

        fnl_dict = {}
        fnl_lst=[]
        fnl_lst.append(start.value)
        fnl_dict[0]=fnl_lst

        while len(tmp)!=0:

            node=tmp.pop(0)
            if node.left!=None:
                val=dict[node.value]

                if (val-1) in fnl_dict.keys():
                    fnl_dict[val-1].append(node.left.value)
                else:
                    fnl_lst=[]
                    fnl_lst.append(node.left.value)
                    fnl_dict[val-1]=fnl_lst
                tmp.append(node.left)
                dict[node.left.value]=val-1

            if node.right != None:
                val = dict[node.value]

                if (val + 1) in fnl_dict.keys():
                    fnl_dict[val + 1].append(node.right.value)
                else:
                    fnl_lst = []
                    fnl_lst.append(node.right.value)
                    fnl_dict[val + 1] = fnl_lst
                tmp.append(node.right)
                dict[node.right.value]=val+1

        for key,val in fnl_dict.items():
            print(key,val)


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
    tree.VerticalOrderTraversalBinaryTree()

if __name__=='__main__':
    main()