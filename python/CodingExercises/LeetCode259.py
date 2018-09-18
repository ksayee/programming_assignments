'''
259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
'''

import collections

def LeetCode259(ary,k):

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

    if len(tmp)==3:

        sum=0
        for l in tmp:
            sum=sum+l
        if sum<k:
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

    ary=[-2,0,1,3]
    k=2
    print(LeetCode259(ary,k))

if __name__=='__main__':
    main()