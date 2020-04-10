'''
I received an email from the recruiter asking me to select a date for a phone interview.
On the day of the interview, the interviewer called me, asked me a few questions about my current role.
Then he shared the question with me on a shared HackerRank link. At the end of the interview, he offered to answer any questions I might have.
I asked him a question about mentorship and training for engineers at Bloomberg.
Question:
An intelligence officer has intercepted a payload over-the-wire.
Some of the engineers have been able to reconstruct it into it's original data structure (a binary tree).
Each node in the tree represents a char. A credible source believes the message will reveal itself by printing the characters
from left-to-right (ie. starting with the leftmost node and working your way over to the rightmost node).
Write an algorithm that decrypts the message. (See input #1 for example)
Examples:

1.
        i
       / \
      r   y
     / \
    p   v

 result: privy

 2.
        a
       /
      i
     /
    c

 result: cia

 3.
         c
          \
           i
            \
             a

 result: cia

 4.
         r
        / \
       e   t
          /
         e
        /
       c
      /
     s

 result: secret

 5.
         e
        / \
       s   r
        \
         c
          \
           e
            \
             t

 result: secret
 '''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree(object):
    def __init__(self,value):
        self.root=Node(value)

    def Preorder(self,start,tmp):
        if start is None:
            return
        tmp.append(start.value)
        self.Preorder(start.left,tmp)
        self.Preorder(start.right,tmp)

    def PrintTree(self):
        start=self.root
        tmp=[]
        self.Preorder(start,tmp)
        return '-'.join(tmp)

    def DecodeMessage(self):
        start=self.root
        node_lst=[]
        node_lst.append(start)
        dict={}
        dict[0]=[]
        dict[0].append(start.value)

        node_dict={}
        node_dict[start.value]=0

        node_lst.append('NONE')

        while len(node_lst)!=0:
            while node_lst[0]!='NONE':
                n=node_lst[0]
                node_lst.pop(0)
                if n.left!=None:
                    val=node_dict[n.value]
                    if val-1 in dict.keys():
                        dict[val-1].append(n.left.value)
                    else:
                        dict[val-1]=[]
                        dict[val-1].append(n.left.value)
                    node_dict[n.left.value]=val-1
                    node_lst.append(n.left)
                if n.right!=None:
                    val = node_dict[n.value]
                    if val + 1 in dict.keys():
                        dict[val + 1].append(n.right.value)
                    else:
                        dict[val + 1] = []
                        dict[val + 1].append(n.right.value)
                    node_dict[n.right.value]=val+1
                    node_lst.append(n.right)
            if len(node_lst)==1 and node_lst[0]=='NONE':
                break
            else:
                node_lst.pop(0)
                node_lst.append('NONE')
        decrypt_lst=[]
        for tup in sorted(dict.items(),key=lambda x:x[0]):
            val=tup[1]
            for element in val:
                decrypt_lst.append(element)
        return ''.join(decrypt_lst)

def main():

    tree=BinaryTree('i')
    tree.root.left=Node('r')
    tree.root.right = Node('y')
    tree.root.left.left = Node('p')
    tree.root.left.right = Node('v')
    print(tree.DecodeMessage())

    tree = BinaryTree('a')
    tree.root.left = Node('i')
    tree.root.left.left = Node('c')
    print(tree.DecodeMessage())

    tree = BinaryTree('c')
    tree.root.right = Node('i')
    tree.root.right.right = Node('a')
    print(tree.DecodeMessage())

    tree = BinaryTree('r')
    tree.root.left = Node('e')
    tree.root.right = Node('t')
    tree.root.right.left = Node('e')
    tree.root.right.left.left = Node('c')
    tree.root.right.left.left.left = Node('s')
    print(tree.DecodeMessage())

    tree = BinaryTree('e')
    tree.root.left = Node('s')
    tree.root.right = Node('r')
    tree.root.left.right = Node('c')
    tree.root.left.right.right = Node('e')
    tree.root.left.right.right.right = Node('t')
    print(tree.DecodeMessage())

if __name__=='__main__':
    main()