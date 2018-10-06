'''
Check if all leaves are at same level
Given a Binary Tree, check if all leaves are at same level or not.
          12
        /    \
      5       7
    /          \
   3            1
  Leaves are at same level

          12
        /    \
      5       7
    /
   3
   Leaves are Not at same level


          12
        /
      5
    /   \
   3     9
  /      /
 1      2
 Leaves are at same level
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

    def LeafsSameLevelBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append("NONE")
        height=0
        fnl_lst=[]
        while len(node_lst)!=0:
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left is None and n.right is None:
                    tup=(n.value,height)
                    fnl_lst.append(tup)
                if n.left !=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            if node_lst[0]=='NONE' and len(node_lst)==1:
                break
            height=height+1
            node_lst.pop(0)
            node_lst.append("NONE")
        print(fnl_lst)
        leaf_lst=[]
        for key in fnl_lst:
            leaf_lst.append(key[1])
        if len(set(leaf_lst))==1:
            return True
        else:
            return False


def main():

    tree=BinaryTree(12)
    tree.root.left=Node(5)
    tree.root.left.left=Node(3)
    tree.root.left.right = Node(9)
    tree.root.left.left.left = Node(1)
    tree.root.left.right.left = Node(2)
    print(tree.print_tree('preorder'))
    print(tree.LeafsSameLevelBinaryTree())

if __name__=='__main__':
    main()