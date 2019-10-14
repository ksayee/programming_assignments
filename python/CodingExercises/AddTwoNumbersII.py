'''
445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

class Node(object):
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.tail=None

    def AddDigit(self,value):
        if self.head==None:
            node=Node(value)
            self.head=node
            self.tail=node
        else:
            node=Node(value)
            self.tail.next=node
            self.tail=node

    def PrintList(self):
        start=self.head
        tmp=[]
        while start!=None:
            tmp.append(str(start.data))
            start=start.next
        return '-'.join(tmp)

    def ReverseRecur(self,start):
        if start.next==None:
            self.head=start
            return start
        tmp=self.ReverseRecur(start.next)
        tmp.next=start
        start.next=None
        self.tail=start
        return start

    def ReverseList(self):
        start=self.head
        self.ReverseRecur(start)
        print(self.PrintList())

    def GetListLength(self,start):
        cnt=1
        while start.next!=None:
            start=start.next
            cnt=cnt+1
        return cnt

    def AddTwoNumbers(self,lst2):
        start=self.head
        len_lst1=self.GetListLength(start)
        start=lst2.head
        len_lst2=self.GetListLength(start)

        if len_lst1>len_lst2:
            big_lst_start=self.head
            sml_lst_start=lst2.head
        else:
            big_lst_start=lst2.head
            sml_lst_start=self.head

        carry=0
        fnl_lst=LinkedList()
        sum=0
        while big_lst_start!=None:
            if sml_lst_start!=None:
                sum=big_lst_start.data+sml_lst_start.data+carry
                sml_lst_start=sml_lst_start.next
            else:
                sum=big_lst_start.data+carry
            big_lst_start=big_lst_start.next
            rem=sum%10
            carry=sum//10
            n=Node(rem)
            if fnl_lst.head==None:
                fnl_lst.head=n
                start=fnl_lst.head
            else:
                start.next=n
                start=start.next
        if carry>0:
            n=Node(carry)
            start.next=n
        fnl_lst.ReverseList()
        return fnl_lst

def main():

    lst1=LinkedList()
    lst1.AddDigit(7)
    lst1.AddDigit(2)
    lst1.AddDigit(4)
    lst1.AddDigit(3)
    print(lst1.PrintList())

    lst2 = LinkedList()
    lst2.AddDigit(5)
    lst2.AddDigit(6)
    lst2.AddDigit(4)
    print(lst2.PrintList())

    lst1.ReverseList()
    lst2.ReverseList()

    fnl_lst=lst1.AddTwoNumbers(lst2)
    print(fnl_lst.PrintList())

if __name__=='__main__':
    main()