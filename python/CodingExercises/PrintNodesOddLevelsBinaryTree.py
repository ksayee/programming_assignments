'''
Print the nodes at odd levels of a tree
Given a binary tree, print nodes of odd level in any order. Root is considered at level 1.

For example consider the following tree
          1
       /     \
      2       3
    /   \       \
   4     5       6
        /  \     /
       7    8   9

Output  1 4 5 6
'''

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

    def PrintNodesOddLevelsBinaryTree(self):

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
            node_lst.append('NONE')
            height=height+1
            fnl_dict[height]=tmp

        sort_lst=sorted(fnl_dict.items(),key=lambda x:x[0])
        out_lst=[]
        for key in sort_lst:
            if key[0]%2!=0:
                out_lst.extend(key[1])
        return out_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right=Node(5)
    tree.root.left.right.left = Node(7)
    tree.root.left.right.right = Node(8)
    tree.root.right.right = Node(6)
    tree.root.right.right.left = Node(9)
    print(tree.print_tree('preorder'))
    print(tree.PrintNodesOddLevelsBinaryTree())

if __name__=='__main__':
    main()