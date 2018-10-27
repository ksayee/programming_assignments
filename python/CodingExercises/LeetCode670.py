'''
671. Maximum Swap
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
'''

import collections

def DoValidate(tmp,num):

    flg=True
    chg=0
    for i in range(0,len(tmp)):
        if tmp[i]!=num[i]:
            chg=chg+1
        if chg>2:
            flg=False
            break
    return flg

def LeetCode670(n):

    num=str(n)

    dict=collections.Counter(num)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,num)

    return sorted(fnl_lst,reverse=True)[0]

def Combinations_recur(lst,cnt,tmp,fnl_lst,num):

    if len(tmp)==len(num):
        flg=DoValidate(tmp,num)
        if flg==True:
            fnl_lst.append(int(''.join(tmp)))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, num)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    n=2736
    print(LeetCode670(n))

    n = 9973
    print(LeetCode670(n))

if __name__=='__main__':
    main()