'''
634. Find the Derangement of An Array
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
'''

import collections

def Validate_Dearrangement(lst,ary):

    flg=True
    for i in range(0,len(lst)):
        if lst[i]==ary[i]:
            flg=False
            break

    return flg

def LeetCode634(n):

    i=1
    ary=[]
    while i<=n:
        ary.append(i)
        i=i+1

    lst=[]
    cnt=[]

    dict=collections.Counter(ary)

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]
    Combinations_recur(ary,lst,cnt,fnl_lst,tmp)

    return fnl_lst

def Combinations_recur(ary,lst,cnt,fnl_lst,tmp):

    if len(tmp)==len(ary):
        flg=Validate_Dearrangement(tmp,ary)
        if flg==True:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(ary, lst, cnt, fnl_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1


def main():

    n=3
    print(LeetCode634(n))

    n = 4
    print(LeetCode634(n))

if __name__=='__main__':
    main()