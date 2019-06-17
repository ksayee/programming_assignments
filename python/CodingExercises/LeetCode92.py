'''
92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def Add(self,value):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def Display(self):
        start=self.head
        fnl_lst=[]
        while start!=None:
            fnl_lst.append(str(start.value))
            start=start.next
        return '-'.join(fnl_lst)

    def Reverse(self,m,n):
        start=self.head
        if m==1:
            flg_head=True
            k=1
        else:
            flg_head=False
            for i in range(1,m-1):
                start=start.next
            node1=start
            k=0
        for i in range(k,n-m):
            start=start.next
        node2=start

        if flg_head==True and node2.next==self.tail:
            tmp=node2.next
            node2.next=self.head
            tmp.next=self.head.next
            self.head=tmp
            self.tail=node2.next
        elif flg_head==True:
            tmp2=node2.next
            tmp1=self.head.next
            node2.next=self.head
            node2.next.next=tmp2.next
            self.head=tmp2
            self.head.next=tmp1
        else:
            tmp2=node2.next
            tmp1=node1.next.next
            node2.next=node1.next
            node2.next.next=tmp2.next
            node1.next=tmp2
            node1.next.next=tmp1

def main():
    
    ll=LinkedList()
    ll.Add(1)
    ll.Add(2)
    ll.Add(3)
    ll.Add(4)
    ll.Add(5)
    print(ll.Display())
    m=2
    n=4
    ll.Reverse(m,n)
    print(ll.Display())

if __name__=='__main__':
    main()