'''
This problem was asked by Microsoft.
Given an array of numbers and a number k,
determine if there are three entries in the array which add up to the specified number k.
For example, given [20, 303, 3, 4, 25] and k = 49, return true as 20 + 4 + 25 = 49.
'''

import collections
def DailyCodingProblem518B(ary,k):
    ary.sort()
    output_lst=[]
    for i in range(0,len(ary)):
        left=i+1
        right=len(ary)-1
        while left<right:
            if ary[i]+ary[left]+ary[right]==k:
                tup=(ary[i],ary[left],ary[right])
                output_lst.append(tup)
                left=left+1
                right=right-1
            elif ary[i]+ary[left]+ary[right]<k:
                left=left+1
            elif ary[i]+ary[left]+ary[right]>k:
                right=right-1
    return output_lst

def Combinations_recur(lst,cnt,tmp,output_lst,k):

    if len(tmp)==3:
        if sum(tmp)==k:
            if sorted(tmp) not in output_lst:
                output_lst.append(sorted(tmp).copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, output_lst, k)
        cnt[i]=cnt[i]+1
        tmp.pop()

def DailyCodingProblem518A(ary,k):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    output_lst=[]
    Combinations_recur(lst,cnt,tmp,output_lst,k)
    return output_lst

def main():

    ary=[20, 303, 3, 4, 25]
    k=49
    print(DailyCodingProblem518A(ary,k))
    print(DailyCodingProblem518B(ary, k))

if __name__=='__main__':
    main()