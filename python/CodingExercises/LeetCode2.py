'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


def LeetCode2(lst1,lst2):

    lst1.reverse()
    lst2.reverse()

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

    lst1 = [5, 4, 3]
    lst2 = [4, 7, 8,9]
    print(LeetCode2(lst1, lst2))


if __name__=='__main__':
    main()