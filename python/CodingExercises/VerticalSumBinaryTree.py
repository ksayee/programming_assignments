'''
Given a Binary Tree, find vertical sum of the nodes that are in same vertical line. Print all sums through different vertical lines.
Examples:

      1
    /   \
  2      3
 / \    / \
4   5  6   7
The tree has 5 vertical lines

Vertical-Line-1 has only one node 4 => vertical sum is 4
Vertical-Line-2: has only one node 2=> vertical sum is 2
Vertical-Line-3: has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3 => vertical sum is 3
Vertical-Line-5: has only one node 7 => vertical sum is 7

So expected output is 4, 2, 12, 3 and 7
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

    def VerticalSumBinaryTree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        dict[start.value]=0
        fnl_dict={}
        tmp=[]
        tmp.append(start.value)
        fnl_dict[0]=tmp

        while len(node_lst)!=0:

            n=node_lst[-1]
            node_lst.pop()

            if n.left!=None:
                val=dict[n.value]

                if val-1 in fnl_dict.keys():
                    fnl_dict[val-1].append(n.left.value)
                else:
                    tmp=[]
                    tmp.append(n.left.value)
                    fnl_dict[val-1]=tmp
                dict[n.left.value]=val-1

            if n.right!=None:
                val=dict[n.value]

                if val+1 in fnl_dict.keys():
                    fnl_dict[val+1].append(n.right.value)
                else:
                    tmp=[]
                    tmp.append(n.right.value)
                    fnl_dict[val+1]=tmp
                dict[n.right.value]=val+1

            if n.left!=None:
                node_lst.append(n.left)
            if n.right!=None:
                node_lst.append(n.right)

        sort_lst=sorted(fnl_dict.items(),key=lambda x:x[0])
        out_lst=[]
        for key in sort_lst:
            sum=0
            for l in key[1]:
                sum=sum+l
            out_lst.append(sum)
        return out_lst

def main():

    tree=BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right=Node(3)
    tree.root.left.left=Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    print(tree.print_tree('preorder'))
    print(tree.VerticalSumBinaryTree())

if __name__=='__main__':
    main()