'''
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''

import collections
def LeetCode179(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(str(key))
        cnt.append(val)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,ary,fnl_lst,tmp)

    max=fnl_lst[0]

    for i in range(1,len(fnl_lst)):
        key=fnl_lst[i]
        if key>max:
            max=key

    return max

def Combinations_recur(lst,cnt,ary,fnl_lst,tmp):

    if len(tmp)==len(ary):
        fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, ary, fnl_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    ary=[10,2]
    print(LeetCode179(ary))

    ary = [3,30,34,5,9]
    print(LeetCode179(ary))

if __name__=='__main__':
    main()