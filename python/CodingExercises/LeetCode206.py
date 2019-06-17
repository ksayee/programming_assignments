'''
206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
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

    def Reverse_recur(self,start):
        if start.next==None:
            self.head=start
            return
        self.Reverse_recur(start.next)
        tmp=start.next
        tmp.next=start
        start.next=None
        self.tail=start

    def Reverse(self):
        start=self.head
        fnl_lst=[]
        self.Reverse_recur(start)


def main():
    
    ll=LinkedList()
    ll.Add(1)
    ll.Add(2)
    ll.Add(3)
    ll.Add(4)
    ll.Add(5)
    print(ll.Display())
    ll.Reverse()
    print(ll.Display())

if __name__=='__main__':
    main()