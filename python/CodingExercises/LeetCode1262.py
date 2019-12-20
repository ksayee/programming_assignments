'''
1262. Greatest Sum Divisible by Three
Medium
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
Example 1:
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
'''

import collections

def Validate(tmp):
    sum=0
    for val in tmp:
        sum=sum+val
    if sum%3==0:
        return sum
    else:
        return -1

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)>0:
        sum=Validate(tmp)
        if sum!=-1:
            if sum in fnl_lst.keys():
                if sorted(tmp) not in fnl_lst[sum]:
                    fnl_lst[sum].append(sorted(tmp).copy())
            else:
                fnl_lst[sum]=[]
                fnl_lst[sum].append(sorted(tmp).copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1262(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst={}
    Combinations_recur(lst,cnt,tmp,fnl_lst)
    if len(fnl_lst)>0:
        return sorted(fnl_lst.items(),key=lambda x:x[0],reverse=True)[0]
    else:
        return 0
        
def main():

    ary=[3,6,5,1,8]
    print(LeetCode1262(ary))

    ary = [4]
    print(LeetCode1262(ary))

    ary = [1,2,3,4,4]
    print(LeetCode1262(ary))

if __name__=='__main__':
    main()