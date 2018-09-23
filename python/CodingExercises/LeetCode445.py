'''
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''

def LeetCode445(ary1,ary2):

    if len(ary1)>len(ary2):
        big_lst=ary1
        sml_lst=ary2
    else:
        big_lst=ary2
        sml_lst=ary1

    fnl_lst=[]

    j=len(sml_lst)-1
    carry=0
    
    for i in range(len(big_lst)-1,-1,-1):

        if j>=0:
            num=big_lst[i]+sml_lst[j]+carry
            j=j-1
        else:
            num=big_lst[i]+carry

        rem=num%10
        fnl_lst.append(str(rem))
        carry=int(num/10)

    if carry>0:
        fnl_lst.append(str(carry))

    fnl_lst.reverse()

    return int(''.join(fnl_lst))



def main():

    ary1=[7,2,4,3]
    ary2=[5,6,4]
    print(LeetCode445(ary1,ary2))

if __name__=='__main__':
    main()