# Sum of all elements in a binary tree

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def preorder(self,start,traversal):
        if start!=None:
            traversal=traversal+ (str(start.value)+ '-')
            traversal=self.preorder(start.left,traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(self.root,'')
        elif traversal_type=='inorder':
            return self.inorder(self.root,'')
        elif traversal_type=='postorder':
            return self.postorder(self.root,'')

    def PrintNodesKDistanceFromRootNodeBinaryTree(self,k):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=0
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[height]=tmp

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    tmp.append(n.left.value)
                    node_lst.append(n.left)
                if n.right!=None:
                    tmp.append(n.right.value)
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            node_lst.pop(0)
            node_lst.append("NONE")
            height=height+1
            fnl_dict[height]=tmp

        out_lst=[]
        for key,val in fnl_dict.items():
            if k==key-0:
                out_lst.extend(val)
        return out_lst


def main():

    tree1=BinaryTree(1)
    tree1.root.left=Node(2)
    tree1.root.right=Node(3)
    tree1.root.left.left=Node(4)
    tree1.root.left.right=Node(5)
    tree1.root.right.left = Node(8)
    print(tree1.print_tree('preorder'))
    k=2
    print(tree1.PrintNodesKDistanceFromRootNodeBinaryTree(k))

if __name__=='__main__':
    main()