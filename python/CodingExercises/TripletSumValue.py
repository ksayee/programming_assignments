# Find a triplet that sum to a given value
# Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
# If there is such a triplet present in array, then print the triplet and return true.
# Else return false. For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24,
# then there is a triplet (12, 3 and 9) present in array whose sum is 24.

import collections
def Combinations_recur(lst,cnt,tmp,output_lst,target):

    if len(tmp)==3:
        if sum(tmp)==target:
            if sorted(tmp) not in output_lst:
                output_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, output_lst,target)
        cnt[i]=cnt[i]+1
        tmp.pop()

def TripletSumValue1(ary,target):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    output_lst=[]
    Combinations_recur(lst,cnt,tmp,output_lst,target)
    return output_lst

def TripletSumValue2(ary, target):

    output_lst=[]
    ary.sort()
    for i in range(0,len(ary)):
        left=i+1
        right=len(ary)-1
        while left < right:
            if ary[i]+ary[left]+ary[right]==target:
                tup=(ary[i],ary[left],ary[right])
                output_lst.append(tup)
                left=left+1
                right=right-1
            elif ary[i]+ary[left]+ary[right]<target:
                left=left+1
            else:
                right=right-1
    return output_lst

def main():

    ary=[12, 3, 4, 1, 6, 9]
    target=24
    print(TripletSumValue1(ary,target))
    print(TripletSumValue2(ary, target))

    ary = [1, 4, 45, 6, 10, 8]
    target = 22
    print(TripletSumValue1(ary,target))
    print(TripletSumValue2(ary, target))

if __name__=='__main__':
    main()