'''
Maximize a number considering permutations with values smaller than limit
Given two numbers N and M. Construct maximal number by permuting (changing order) the digits of N, not exceeding M.
Note : It is allowed to leave N as it is.
Examples:
Input : N = 123, M = 222
Output : 213
There are total 3! permutations possible for N = 123,
But the only permutation that satisfies the given condition is 213.
Similarly, In example 2, there are total 4! permutations possible for N = 3921, But the only permutation that satisfies the given condition is 9321.
Input : N = 3921, M = 10000
Output : 9321
'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst,limit,num):

    if len(tmp)==len(str(num)):
        if int(''.join(tmp))<limit:
            fnl_lst.append(int(''.join(tmp)))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, limit,num)
        cnt[i]=cnt[i]+1
        tmp.pop()

def MaxNumPermutationValueSmallerLimit(num, limit):

    dict=collections.Counter(str(num))
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,limit,num)
    return sorted(fnl_lst,reverse=True)[0]

def main():

    num = 123
    limit=222
    print(MaxNumPermutationValueSmallerLimit(num,limit))

    num = 3921
    limit = 10000
    print(MaxNumPermutationValueSmallerLimit(num, limit))

if __name__=='__main__':
    main()