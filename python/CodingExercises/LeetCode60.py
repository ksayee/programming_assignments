'''
60. Permutation Sequence

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''

import collections

def LeetCode60(n,k):

    ary=[]

    for i in range(1,n+1):
        ary.append(i)

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]
    Permutations_recur(lst,cnt,fnl_lst,tmp,n)

    return fnl_lst[k-1]

def Permutations_recur(lst,cnt,fnl_lst,tmp,n):

    if len(tmp)==n:
        fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Permutations_recur(lst, cnt, fnl_lst, tmp,n)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    n=3
    k=3
    print(LeetCode60(n,k))

    n = 4
    k = 9
    print(LeetCode60(n,k))

if __name__=='__main__':
    main()