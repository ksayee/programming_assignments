'''
This problem was asked by Microsoft.
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.
For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.
Given two linked lists in this format, return their sum in the same linked list format.
For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:
4 -> 2 -> 1
'''

class Node(object):
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList(object):
    def __init__(self,value):
        self.head=Node(value)

    def Print_linkedList(self):
        head=self.head
        while head!=None:
            if head.next==None:
                print(head.value)
            else:
                print(head.value, end='->')
            head=head.next

    def GetList(self):
        head=self.head
        lst=[]
        while head!=None:
            lst.append(head.value)
            head=head.next
        lst.reverse()
        return lst

def DailyCodingProblem127(lst1,lst2):
    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    j=len(sml_lst)-1
    carry=0
    fnl_lst=[]
    for i in range(len(big_lst)-1,-1,-1):
        if j>=0:
            num=big_lst[i]+sml_lst[j]+carry
        else:
            num=big_lst[i]+carry
        rem=num%10
        fnl_lst.append(rem)
        carry=num//10

    if carry>0:
        fnl_lst.append(carry)
    fnl_lst.reverse()
    return fnl_lst

def main():

    ll=LinkedList(1)
    ll.head.next=Node(2)
    ll.head.next.next=Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    ll.Print_linkedList()

    ll_1=LinkedList(9)
    ll_1.head.next=Node(9)
    ll_1.Print_linkedList()

    ll_2 = LinkedList(5)
    ll_2.head.next = Node(2)
    ll_2.Print_linkedList()

    lst1=ll_1.GetList()
    lst2=ll_2.GetList()
    result=DailyCodingProblem127(lst1,lst2)
    print(result)

    rst=LinkedList(result[-1])
    tmp=rst
    rst=rst.head
    i=len(result)-2
    while i>=0:
        rst.next=Node(result[i])
        rst=rst.next
        i=i-1
    rst=tmp
    rst.Print_linkedList()

if __name__=='__main__':
    main()