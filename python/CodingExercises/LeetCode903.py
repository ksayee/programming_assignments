'''
903. Valid Permutations for DI Sequence
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.



Example 1:

Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
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

def LeetCode903(str1):

    i=0
    ary=[]
    while i<=len(str1):
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

    str1='DID'
    print(LeetCode903(str1))

if __name__=='__main__':
    main()