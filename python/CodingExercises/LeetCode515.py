'''
515. Find Largest Value in Each Tree Row
You need to find the largest value in each row of a binary tree.
Example:
Input:
          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(str(start.data))
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintPreorder(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def LeetCode515(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        height=0
        node_lst.append("NONE")
        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!="NONE":
                node=node_lst[0]
                node_lst.pop(0)
                tmp.append(node.data)
                if node.left!=None:
                    node_lst.append(node.left)
                if node.right!=None:
                    node_lst.append(node.right)
            height=height+1
            dict[height]=tmp
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            node_lst.append('NONE')
            node_lst.pop(0)
        fnl_lst=[]
        sort_dict=sorted(dict.items(),key=lambda x:x[0])
        for tup in sort_dict:
            fnl_lst.append(max(tup[1]))
        return fnl_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(3)
    tree.root.right=Node(2)
    tree.root.left.left = Node(5)
    tree.root.left.right = Node(3)
    tree.root.right.right = Node(9)
    print(tree.PrintPreorder())
    print(tree.LeetCode515())

if __name__=='__main__':
    main()