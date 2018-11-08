'''

Input:
A
    B
        C
            D
                E
    F
        K
    G

Output:
        (A)
B       F           G
C       K
D
E
'''

class Node(object):

    def __init__(self,value):
        self.value=value
        self.child=[]

class BinaryTree(object):

    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self):

        start=self.root
        node_lst=[]
        node_lst.append(start)
        node_lst.append('NONE')
        height=0
        dict={}

        while len(node_lst)!=0:
            tmp=[]
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                tmp.append(n.value)
                for i in range(0,len(n.child)):
                    node_lst.append(n.child[i])
            height=height+1
            dict[height]=tmp
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            else:
                node_lst.pop(0)
                node_lst.append('NONE')
        return dict.items()


def main():

    str1='A\n\tB\n\t\tC\n\t\t\tD\n\t\t\t\tE\n\tF\n\t\tK\n\tG'
    lst=str1.split('\n')
    for l in lst:
        tmp=l.split('\t')
        key=tmp[-1]
        level=len(tmp)-1

        if level==0:
            tree=BinaryTree(key)
        elif level==1:
            tree.root.child.append(Node(key))
        elif level==2:
            tree.root.child[0].child.append(Node(key))
        elif level==3:
            tree.root.child[0].child[0].child.append(Node(key))
        elif level==4:
            tree.root.child[0].child[0].child[0].child.append(Node(key))
    print(tree.print_tree())
if __name__=='__main__':
    main()