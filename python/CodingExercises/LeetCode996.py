'''
996. Number of Squareful Arrays
Hard
Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.
Return the number of permutations of A that are squareful.
Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].
Example 1:
Input: [1,17,8]
Output: 2
Explanation:
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:
Input: [2,2,2]
Output: 1
'''
import collections
import math

def Validate(tmp):

    flg=True
    for i in range(1,len(tmp)):
        sum=tmp[i-1]+tmp[i]
        if str(math.sqrt(sum)).split('.')[1]!='0':
            flg=False
            break
    return flg

def Combinations_recur(lst,cnt,tmp,fnl_lst,lgt):

    if len(tmp)==lgt:
        flg=Validate(tmp)
        if flg==True:
            if tmp not in fnl_lst:
                fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, lgt)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode996(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,len(ary))
    return fnl_lst

def main():

    ary=[1,17,8]
    print(LeetCode996(ary))

    ary = [2,2,2]
    print(LeetCode996(ary))

if __name__=='__main__':
    main()