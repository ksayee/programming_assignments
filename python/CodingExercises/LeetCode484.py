'''
484. Find Permutation
By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI",
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]
Note:

The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000
'''

import collections

def Validate_Permutation(lst,str1):

    j=0
    flg=True
    for i in range(1,len(lst)):

        if str1[j]=='I':
            if lst[i]>lst[i-1]:
                j=j+1
            else:
                flg=False
        elif str1[j]=='D':
            if lst[i]<lst[i-1]:
                j=j+1
            else:
                flg=False
    return flg

def LeetCode484(str1):

    i=1
    ary=[]
    while i<=len(str1)+1:
        ary.append(i)
        i=i+1

    lst=[]
    cnt=[]

    dict=collections.Counter(ary)

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]


    Combinations_recur(ary,lst,cnt,fnl_lst,tmp,str1)

    return fnl_lst

def Combinations_recur(ary,lst,cnt,fnl_lst,tmp,str1):

    if len(tmp)==len(ary):
        flg=Validate_Permutation(tmp,str1)
        if flg==True:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(ary, lst, cnt, fnl_lst, tmp,str1)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    str1='I'
    print(LeetCode484(str1))

    str1 = 'DI'
    print(LeetCode484(str1))

if __name__=='__main__':
    main()