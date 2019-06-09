'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
        n=Node(value)
        if self.head==None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n

    def Display(self):
        start=self.head
        while start!=None:
            print(start.value,end="")
            start=start.next
        print()

    def Reverse_Recur(self,start):
        if start.next==None:
            self.head=start
            return
        self.Reverse_Recur(start.next)
        tmp=start.next
        tmp.next=start
        start.next=None

    def reverse(self):
        start=self.head
        self.Reverse_Recur(start)

    def GetLength(self):
        start=self.head
        cnt=0
        if start==None:
            pass
        else:
            while start.next!=None:
                start=start.next
                cnt=cnt+1
        return cnt

    def AddLinkedList(self,lst2):
        self.reverse()
        lst2.reverse()

        cnt1=self.GetLength()
        cnt2=lst2.GetLength()

        if cnt1>cnt2:
            big_head=self.head
            sml_head=lst2.head
        else:
            big_head=lst2.head
            sml_head=self.head

        carry=0
        result_lst=LinkedList()
        while big_head!=None:
            if sml_head!=None:
                num=big_head.value+sml_head.value+carry
                sml_head=sml_head.next
            else:
                num=big_head.value+carry
            big_head=big_head.next
            rem=num%10
            carry=num//10
            result_lst.Add(rem)
        if carry>0:
            result_lst.Add(rem)
        result_lst.reverse()
        return result_lst

def LeetCode2(lst1,lst2):

    sml_lst=[]
    big_lst=[]

    if len(lst1)>len(lst2):
        big_lst=lst1
        sml_lst=lst2
    else:
        big_lst=lst2
        sml_lst=lst1

    j=len(sml_lst)-1
    fnl_lst=[]
    carry=0
    for i in range(len(big_lst)-1,-1,-1):

        if j>=0:
            sum=big_lst[i]+sml_lst[j]+carry
            j=j-1
        else:
            sum=big_lst[i]+carry
        rem=sum%10
        fnl_lst.append(str(rem))
        carry=int(sum/10)

    if carry>0:
        fnl_lst.append(str(carry))
    fnl_lst.reverse()

    return ''.join(fnl_lst)

def main():
    
    lst1=[2,4,3]
    lst2=[5,6,4]
    print(LeetCode2(lst1,lst2))

    lst1=LinkedList()
    lst1.Add(2)
    lst1.Add(4)
    lst1.Add(3)

    lst2 = LinkedList()
    lst2.Add(5)
    lst2.Add(6)
    lst2.Add(4)
    result_lst=lst1.AddLinkedList(lst2)
    result_lst.Display()

    lst1 = [5, 4, 3]
    lst2 = [4, 7, 8,9]
    print(LeetCode2(lst1, lst2))

    lst1 = LinkedList()
    lst1.Add(5)
    lst1.Add(4)
    lst1.Add(3)

    lst2 = LinkedList()
    lst2.Add(4)
    lst2.Add(7)
    lst2.Add(8)
    lst2.Add(9)
    result_lst = lst1.AddLinkedList(lst2)
    result_lst.Display()

if __name__=='__main__':
    main()