'''
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,root):
        self.root=Node(root)

    def PrintPreorder(self,start,tmp):
        if start==None:
            return
        tmp.append(start.value)
        self.PrintPreorder(start.left,tmp)
        self.PrintPreorder(start.right,tmp)


    def PrintTraversal(self,TraversalType):
        start=self.root
        tmp=[]
        if TraversalType=='Preorder':
            self.PrintPreorder(start,tmp)
        return tmp

    def GetDeepestNode(self):
        start=self.root
        node_lst=[]
        dict={}
        node_lst.append(start)
        height=0
        node_lst.append('NONE')
        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                tmp.append(n.value)
                if n.left!=None:
                    node_lst.append(n.left)
                if n.right!=None:
                    node_lst.append(n.right)
            height=height+1
            dict[height]=tmp
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            else:
                node_lst.pop(0)
                node_lst.append('NONE')
        print(dict)
        return sorted(dict.items(),key=lambda x:x[0],reverse=True)[0][1]
        
def main():

    tree=BinaryTree('A')
    tree.root.left=Node('B')
    tree.root.right=Node('C')
    tree.root.left.left=Node('D')
    print(tree.PrintTraversal('Preorder'))
    print(tree.GetDeepestNode())

if __name__=='__main__':
    main()