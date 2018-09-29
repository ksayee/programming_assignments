'''
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

import collections

def LeetCode78(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]

    Combinations_recur(ary,lst,cnt,tmp,fnl_lst)

    return fnl_lst

def Combinations_recur(ary,lst,cnt,tmp,fnl_lst):

    if len(tmp)<=len(ary):
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(ary,lst, cnt, tmp, fnl_lst)
        tmp.pop()
        cnt[i]=cnt[i]+1



def main():

    ary=[1,2,3]
    print(LeetCode78(ary))

if __name__=='__main__':
    main()