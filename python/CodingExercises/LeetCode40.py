'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

import collections

def LeetCode40(ary,k):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    res_lst=[]
    tmp=[]
    Combinations_recur(lst,cnt,res_lst,tmp,k)

    return res_lst

def Combinations_recur(lst,cnt,res_lst,tmp,k):

    if len(tmp)>0:
        sum=0
        for l in tmp:
            sum=sum+l
        if sum==k:
            if sorted(tmp) not in res_lst:
                res_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, res_lst, tmp, k)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    ary=[10,1,2,7,6,1,5]
    k=8
    print(LeetCode40(ary,k))

    ary = [2,5,2,1,2]
    k = 5
    print(LeetCode40(ary, k))

if __name__=='__main__':
    main()