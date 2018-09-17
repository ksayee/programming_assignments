'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

import collections

def LeetCode47(ary):

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
    
    ary=[1,1,2]
    print(LeetCode47(ary))

    ary = [1, 2, 2,3,3,4]
    print(LeetCode47(ary))

if __name__=='__main__':
    main()