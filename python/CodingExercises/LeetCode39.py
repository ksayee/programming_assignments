'''
39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

import collections

def LeetCode39(ary, k):

    fnl_lst=[]
    tmp=[]
    Combinations_recur(ary,fnl_lst,tmp,k)

    return fnl_lst

def Combinations_recur(ary,fnl_lst,tmp,k):

    if k==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(ary)):

        if ary[i]>k:
            break
        tmp.append(ary[i])
        Combinations_recur(ary, fnl_lst, tmp, k-ary[i])
        tmp.pop()

def main():

    ary=[2,3,6,7]
    k=7
    print(LeetCode39(ary,k))

    ary = [2,3,5]
    k = 8
    print(LeetCode39(ary, k))

if __name__=='__main__':
    main()