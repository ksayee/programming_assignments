'''
Find the middle of a given linked list in C and Java
Given a singly linked list, find middle of the linked list.
For example, if given linked list is 1->2->3->4->5 then output should be 3.

If there are even nodes, then there would be two middle nodes, we need to print second middle element.
For example, if given linked list is 1->2->3->4->5->6 then output should be 4.
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def Add(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=node

    def DisplayList(self):
        start=self.head
        output_lst=[]
        while start!=None:
            output_lst.append(start.value)
            start=start.next
        return output_lst

    def FindMiddleElement(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while True:
            if fast_ptr is None:
                return slow_ptr.value
            if fast_ptr.next is None:
                return slow_ptr.value
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next

def main():

    ll=LinkedList()
    ll.Add(1)
    ll.Add(2)
    ll.Add(3)
    ll.Add(4)
    ll.Add(5)
    print(ll.DisplayList())
    print(ll.FindMiddleElement())

    ll = LinkedList()
    ll.Add(1)
    ll.Add(2)
    ll.Add(3)
    ll.Add(4)
    ll.Add(5)
    ll.Add(6)
    print(ll.DisplayList())
    print(ll.FindMiddleElement())

if __name__=='__main__':
    main()