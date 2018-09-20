'''
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

import collections

def LeetCode216(ary,k,n):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,fnl_lst,tmp,k,n)

    return fnl_lst

def Combinations_recur(lst,fnl_lst,tmp,k,n):


    if len(tmp)==k:
        sum=0
        for l in tmp:
            sum=sum+l
        if sum==n:
            if sorted(tmp) not in fnl_lst:
                fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        tmp.append(lst[i])
        Combinations_recur(lst[i+1:], fnl_lst, tmp, k, n)
        tmp.pop()


def main():

    k=3
    n=7
    ary=[1,2,3,4,5,6,7,8,9]
    print(LeetCode216(ary,k,n))

    k = 3
    n = 9
    ary = [1,2,3,4,5,6,7,8,9]
    print(LeetCode216(ary,k, n))

if __name__=='__main__':
    main()