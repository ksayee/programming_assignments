# Find the closest pair from two sorted arrays
# Given two sorted arrays and a number x,
# find the pair whose sum is closest to x and the pair has an element from each array.
# We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x,
# we need to find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.

def ClosestPairsSortedArraysIterative(ary1,ary2,k):

    diff=999
    fnl_lst=[]

    for i in range(0,len(ary1)):
        for j in range(0,len(ary2)):

            sum=ary1[i]+ary2[j]

            if abs(k-sum)<diff:
                diff=abs(k-sum)
                fnl_lst=[]
                fnl_lst.append((ary1[i],ary2[j]))

    return fnl_lst

def ClosestPairsSortedArrays(ary1,ary2,k):

    diff=9999

    l=0
    r=len(ary2)-1

    res_l=0
    res_r=0

    while l<len(ary1) and r>=0:

        sum=ary1[l]+ary2[r]

        if abs(k-sum)<diff:
            res_l=l
            res_r=r
            diff=abs(k-sum)

        if ary1[l]+ary2[r]>k:
            r=r-1
        else:
            l=l+1

    fnl_lst=[]
    fnl_lst.append((ary1[res_l], ary2[res_r]))

    return fnl_lst

def main():

    ary1=[1, 4, 5, 7]
    ary2 = [10, 20, 30, 40]
    k=32
    print(ClosestPairsSortedArrays(ary1,ary2,k))
    print(ClosestPairsSortedArraysIterative(ary1, ary2, k))

    ary1 = [1, 4, 5, 7]
    ary2 = [10, 20, 30, 40]
    k = 50
    print(ClosestPairsSortedArrays(ary1, ary2, k))
    print(ClosestPairsSortedArraysIterative(ary1, ary2, k))

if __name__=='__main__':
    main()