'''
989. Add to Array-Form of Integer
Easy
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].
Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
Example 1:
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
'''
import collections
import math

def LeetCode989(ary, num):

    ary2=[]
    while num!=0:
        rem=num%10
        num=num//10
        ary2.append(rem)
    ary2.reverse()

    if len(ary)>len(ary2):
        big_lst=ary
        sml_lst=ary2
    else:
        big_lst=ary2
        sml_lst=ary

    carry=0
    j=len(sml_lst)-1
    fnl_lst=[]
    for i in range(len(big_lst)-1,-1,-1):

        if j>=0:
            sum=big_lst[i]+sml_lst[j]+carry
            j=j-1
        else:
            sum=big_lst[i]+carry
        rem=sum%10
        fnl_lst.append(rem)
        carry=sum//10
    if carry>0:
        fnl_lst.append(carry)
    fnl_lst.reverse()
    return fnl_lst

def main():

    ary=[1,2,0,0]
    num=34
    print(LeetCode989(ary,num))

    ary = [2,7,4]
    num = 181
    print(LeetCode989(ary, num))

    ary = [2,1,5]
    num = 806
    print(LeetCode989(ary, num))

    ary = [9,9,9,9,9,9,9,9,9,9]
    num = 1
    print(LeetCode989(ary, num))

if __name__=='__main__':
    main()