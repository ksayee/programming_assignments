'''
Make middle node head in a linked list
Given a singly linked list, find middle of the linked list and set middle node of the linked list at beginning of the linked list.
Examples:
Input  : 1 2 3 4 5
Output : 3 1 2 4 5
Input  : 1 2 3 4 5 6
Output : 4 1 2 3 5 6
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

    def MakeMiddleNodeHead(self):
        slow_ptr=self.head
        fast_ptr=self.head
        prev_node=None
        while True:
            if fast_ptr is None:
                break
            if fast_ptr.next is None:
                break
            prev_node=slow_ptr
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next

        prev_node.next=slow_ptr.next
        slow_ptr.next=self.head
        self.head=slow_ptr


def main():

    ll=LinkedList()
    ll.Add(1)
    ll.Add(2)
    ll.Add(3)
    ll.Add(4)
    ll.Add(5)
    print(ll.DisplayList())
    ll.MakeMiddleNodeHead()
    print(ll.DisplayList())

    ll = LinkedList()
    ll.Add(1)
    ll.Add(2)
    ll.Add(3)
    ll.Add(4)
    ll.Add(5)
    ll.Add(6)
    print(ll.DisplayList())
    ll.MakeMiddleNodeHead()
    print(ll.DisplayList())

if __name__=='__main__':
    main()