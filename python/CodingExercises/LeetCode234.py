'''
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false
Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
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

    def Reverse_Recur(self,start):
        if start.next==None:
            self.head=start
            return
        self.Reverse_Recur(start.next)
        tmp=start.next
        tmp.next=start
        start.next=None

    def Reverse(self):
        start=self.head
        self.Reverse_Recur(start)

    def ReturnStringLinkedList(self):
        fnl_lst=[]
        start=self.head
        while start.next!=None:
            fnl_lst.append(str(start.value))
            start=start.next
        return ''.join(fnl_lst)

    def CheckPalindrome(self):
        original_str=self.ReturnStringLinkedList()
        self.Reverse()
        new_str=self.ReturnStringLinkedList()
        if original_str==new_str:
            return True
        else:
            return False

def main():
    
    lst1=LinkedList()
    lst1.Add(1)
    lst1.Add(2)
    print(lst1.CheckPalindrome())

    lst1 = LinkedList()
    lst1.Add(1)
    lst1.Add(2)
    lst1.Add(2)
    lst1.Add(1)
    print(lst1.CheckPalindrome())

if __name__=='__main__':
    main()