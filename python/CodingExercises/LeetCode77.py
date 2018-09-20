'''
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

import collections

def LeetCode77(n, k):

    ary=[]
    i=1
    while i<=4:
        ary.append(i)
        i=i+1
    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp,k)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp,k):

    if len(tmp)==k:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp, k)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    n=4
    k=2
    print(LeetCode77(n,k))

    n = 5
    k = 3
    print(LeetCode77(n, k))

if __name__=='__main__':
    main()