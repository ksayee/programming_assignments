# Number of substrings divisible by 6 in a string of integers
# Given a string consisting of integers 0 to 9.
# The task is to count the number of substrings which when convert into integer are divisible by 6.
# Substring does not contain leading zeroes.

import collections

def IntegerSubstringDivisibleBy6(str1):

    dict=collections.Counter(str1)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    res=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,res,fnl_lst)

    result=[]
    for i in range(0,len(fnl_lst)):
        num=int(fnl_lst[i])
        if num%6==0:
            result.append(num)
    return list(set(result))

def Combinations_recur(lst,cnt,res,fnl_lst):

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        res.append(lst[i])
        fnl_lst.append(''.join(res))
        cnt[i]=cnt[i]-1
        Combinations_recur(lst,cnt,res,fnl_lst)
        res.pop()
        cnt[i]=cnt[i]+1
    return

def main():

    str1='606'
    print(IntegerSubstringDivisibleBy6(str1))

    str1= '4806'
    print(IntegerSubstringDivisibleBy6(str1))

if __name__=='__main__':
    main()