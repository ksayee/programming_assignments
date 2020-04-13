'''
876. Middle of the Linked List
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def Add(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=n

    def DisplayList(self):
        start=self.head
        tmp=[]
        while start!=None:
            tmp.append(str(start.value))
            start=start.next
        return '-->'.join(tmp)

    def FindMiddleElement(self):
        slow_ptr=self.head
        fast_ptr=slow_ptr.next.next

        while True:
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
            if fast_ptr==None:
                return slow_ptr.next.value
            elif fast_ptr.next==None:
                return slow_ptr.next.value

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