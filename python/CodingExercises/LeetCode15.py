'''
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def LeetCode15(ary):

    fnl_lst=[]
    k=0

    for i in range(0,len(ary)):
        dict={}
        for j in range(i+1,len(ary)):

            sum=ary[i]+ary[j]

            diff=k-sum

            if diff in dict.keys():
                tup=tuple(sorted((ary[i],ary[j],diff)))
                if tup not in fnl_lst:
                    fnl_lst.append(tup)
            else:
                dict[ary[j]]=1

    return fnl_lst

import collections
def LeetCode15_recur(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp):

    if len(tmp)==3:
        sum=0
        for l in tmp:
            sum=sum+l
        if sum==0:
            if sorted(tmp) not in fnl_lst:
                fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    ary=[-1, 0, 1, 2, -1, -4]
    print(LeetCode15(ary))
    print(LeetCode15_recur(ary))

if __name__=='__main__':
    main()