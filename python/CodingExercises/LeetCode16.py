'''
https://leetcode.com/problems/3sum-closest/description/
16. 3Sum Closest

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

import collections
def LeetCode16(ary,k):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    res_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,res_lst,tmp)

    fnl_dict={}
    for lst in res_lst:
        sum=0
        for l in lst:
            sum=sum+l
        diff=abs(k-sum)
        if diff in fnl_dict.keys():
            fnl_dict[diff].append(lst)
        else:
            tmp=[]
            tmp.append(lst)
            fnl_dict[diff]=tmp

    return sorted(fnl_dict.items(),key=lambda x:x[0])[0]

def Combinations_recur(lst,cnt,res_lst,tmp):

    if len(tmp)==3:
        if sorted(tmp) not in res_lst:
            res_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, res_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    ary=[-1, 2, 1, -4]
    k=1
    print(LeetCode16(ary,k))

if __name__=='__main__':
    main()