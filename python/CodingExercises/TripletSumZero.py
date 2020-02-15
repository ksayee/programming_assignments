# Find all triplets with zero sum
# Given an array of distinct elements.
# The task is to find triplets in array whose sum is zero.

import collections

def Combinations_recur(lst,cnt,tmp,output_lst):

    if len(tmp)==3:
        val_sum=sum(tmp)
        if val_sum==0:
            if sorted(tmp) not in output_lst:
                output_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, output_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def TripletSumZero1(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    output_lst=[]
    Combinations_recur(lst,cnt,tmp,output_lst)
    return output_lst

def TripletSumZero2(ary):

    ary.sort()
    output_lst=[]
    for i in range(0,len(ary)):
        left=i+1
        right=len(ary)-1
        while left < right:
            if ary[left]+ary[right]+ary[i]==0:
                tup=(ary[i],ary[left],ary[right])
                if tup not in output_lst:
                    output_lst.append(tup)
                left=left+1
                right=right-1
            elif ary[left]+ary[right]+ary[i]<0:
                left=left+1
            else:
                right=right-1
    return output_lst

def main():

    ary=[0, -1, 2, -3, 1]
    print(TripletSumZero1(ary))
    print(TripletSumZero2(ary))

    ary = [1, -2, 1, 0, 5]
    print(TripletSumZero1(ary))
    print(TripletSumZero2(ary))

    ary=[-1, 0, 1, 2, -1, -4]
    print(TripletSumZero1(ary))
    print(TripletSumZero2(ary))

if __name__=='__main__':
    main()