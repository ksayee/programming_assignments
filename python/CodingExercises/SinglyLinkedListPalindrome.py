# Check if a singly Linked List is a Palindrome

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def add(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
        else:
            start=self.head
            while start.next!=None:
                start=start.next
            start.next=node

    def display(self):
        lst=[]
        start=self.head
        while start!=None:
            lst.append(str(start.value))
            start=start.next
        return '-'.join(lst)

    def reverse(self,node):
        prev_node=None
        curr_node=node
        next_node=None

        while curr_node!=None:
            next_node=curr_node.next
            curr_node.next=prev_node
            prev_node=curr_node
            curr_node=next_node
        return prev_node

    def PalindromeCheck(self):
        slow_ptr=self.head
        fast_ptr=self.head

        while True:
            fast_ptr=fast_ptr.next.next
            if fast_ptr==None:
                second_start=slow_ptr.next
                break
            if fast_ptr.next==None:
                second_start=slow_ptr.next.next
                break
            slow_ptr=slow_ptr.next
        second_start=self.reverse(second_start)
        start=self.head

        while second_start!=None:
            if start.value!=second_start.value:
                return False
            else:
                start=start.next
                second_start=second_start.next
        return True

def main():
    ll=LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(30)
    ll.add(20)
    ll.add(10)
    print(ll.display())
    print(ll.PalindromeCheck())
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)
    ll.add(30)
    ll.add(20)
    ll.add(10)
    print(ll.display())
    print(ll.PalindromeCheck())

if __name__=='__main__':
    main()