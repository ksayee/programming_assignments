'''
1171. Remove Zero Sum Consecutive Nodes from Linked List
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
After doing so, return the head of the final linked list.  You may return any such answer.
(Note that in the examples below, all sequences are serializations of ListNode objects.)
Example 1:
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:
Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:
Input: head = [1,2,3,-3,-2]
Output: [1]
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def add(self,value):
        n=Node(value)
        if self.head is None:
            self.head=n
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=n

    def RemoveConsecutiveSum(self):
        dict={}
        sum=0
        start=self.head
        while start!=None:
            sum=sum+start.value
            if sum not in dict.keys():
                dict[sum]=start
            else:
                node=dict[sum]
                node.next=start.next
            start=start.next

    def Display(self):
        start=self.head
        lst=[]
        while start!=None:
            lst.append(start.value)
            start=start.next
        return lst

def main():

    ll=LinkedList()
    ll.add(3)
    ll.add(4)
    ll.add(2)
    ll.add(-6)
    ll.add(1)
    ll.add(1)
    ll.add(5)
    ll.add(-6)
    print(ll.Display())
    ll.RemoveConsecutiveSum()
    print(ll.Display())

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(-3)
    ll.add(3)
    ll.add(1)
    print(ll.Display())
    ll.RemoveConsecutiveSum()
    print(ll.Display())

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(-3)
    ll.add(4)
    print(ll.Display())
    ll.RemoveConsecutiveSum()
    print(ll.Display())

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(-3)
    ll.add(-2)
    print(ll.Display())
    ll.RemoveConsecutiveSum()
    print(ll.Display())

if __name__=='__main__':
    main()