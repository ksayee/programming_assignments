'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

import collections

def LeetCode46(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    res_lst=[]
    tmp=[]
    Permutations_recur(ary,lst,cnt,res_lst,tmp)

    return res_lst

def Permutations_recur(ary,lst,cnt,res_lst,tmp):

    if len(tmp)==len(ary):
        res_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Permutations_recur(ary,lst, cnt, res_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    ary=[1,2,3]
    print(LeetCode46(ary))

    ary = [1, 2, 3,4,5,6,7]
    print(LeetCode46(ary))

if __name__=='__main__':
    main()