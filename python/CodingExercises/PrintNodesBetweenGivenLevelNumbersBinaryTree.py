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

    def PrintNodesBetweenGivenLevelNumbersBinaryTree(self,low,high):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=1
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

        sort_lst=sorted(fnl_dict.items(),key=lambda x:x[0])
        for key in sort_lst:
            if key[0]>=low and key[0]<=high:
                print(key[1])


def main():

    tree1=BinaryTree(20)
    tree1.root.left=Node(8)
    tree1.root.right=Node(22)
    tree1.root.left.left=Node(4)
    tree1.root.left.right=Node(12)
    tree1.root.left.right.left = Node(10)
    tree1.root.left.right.right = Node(14)
    print(tree1.print_tree('preorder'))
    low=2
    high=4
    tree1.PrintNodesBetweenGivenLevelNumbersBinaryTree(low,high)

if __name__=='__main__':
    main()