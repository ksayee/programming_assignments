'''
922. Sort Array By Parity II
Easy
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.
Example 1:
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''

def Validate(tmp):

    flg=True
    for i in range(0,len(tmp)):

        if i%2==0 and tmp[i]%2==0:
            pass
        elif i%2!=0 and tmp[i]%2!=0:
            pass
        else:
            flg=False
            break
    return flg

def Combination_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==len(lst):
        flg=Validate(tmp)
        if flg==True:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combination_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

import collections
def LeetCode922(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combination_recur(lst,cnt,tmp,fnl_lst)
    return fnl_lst

def main():

    ary=[4,2,5,7]
    print(LeetCode922(ary))

if __name__=='__main__':
    main()