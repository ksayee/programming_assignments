'''
1099.Two Sum Less Than K
Given an array A of integers and integer K, return the maximum S such that
there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.
Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:
Input: A = [10,20,30], K = 15
Output: -1
Explanation:
In this case it's not possible to get a pair sum less that 15.
'''

import collections

def GetSum(tmp,k):

    sum=0
    for l in tmp:
        sum=sum+l
    if sum<k:
        return sum
    else:
        return -1

def Combinations_recur(lst,cnt,tmp,fnl_lst,k):

    if len(tmp)==2:
        sum=GetSum(tmp,k)
        if sum not in fnl_lst:
            fnl_lst.append(sum)
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, k)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1099(ary, k):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,k)

    return sorted(fnl_lst,reverse=True)[0]

def main():

    ary=[34,23,1,24,75,33,54,8]
    k=60
    print(LeetCode1099(ary,k))

    ary = [10,20,30]
    k = 15
    print(LeetCode1099(ary, k))

if __name__=='__main__':
    main()