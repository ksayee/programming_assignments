'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


def LeetCode67(a,b):

    if len(a)>len(b):
        big_lst=list(a)
        sml_lst=list(b)
    else:
        big_lst=list(b)
        sml_lst=list(a)

    fnl_lst=[]

    j=len(sml_lst)-1
    carry=0
    for i in range(len(big_lst)-1,-1,-1):

        if j>=0:
            sum=int(big_lst[i])+int(sml_lst[j])+carry
            j=j-1
        else:
            sum=int(big_lst[i])+carry

        if sum>1:
            rem=0
            carry=1
        else:
            rem=sum
            carry=0

        fnl_lst.append(str(rem))

    if carry>0:
        fnl_lst.append(str(1))

    fnl_lst.reverse()

    return ''.join(fnl_lst)


def main():
    
    a='11'
    b='1'
    print(LeetCode67(a,b))

    a = '1010'
    b = '1011'
    print(LeetCode67(a, b))

if __name__=='__main__':
    main()