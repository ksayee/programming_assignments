'''
Missing Element in Sorted Array
Link: Missing Element in Sorted Array

Problem description
Given a sorted array A of unique numbers, find the *K*-th missing number starting from the leftmost number of the array.

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation:
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation:
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation:
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
'''

def LeetCode1060(ary,k):

    left=0
    right=len(ary)-1
    fnl_lst=[]

    while left<right:
        mid=int((left+right)/2)
        miss_nums=(ary[mid]-ary[left]+1)-(mid-left+1)
        if k<=miss_nums:
            right=mid
        else:
            left=mid
            k=k-miss_nums
        if mid-left==1 or mid -left==0:
            break

    temp=ary[left]+1
    m=k
    while temp<ary[right]:
        if temp not in ary:
            fnl_lst.append(temp)
        temp=temp+1
        m=m-1
    while m>=0:
        if temp not in ary:
            fnl_lst.append(temp)
        temp=temp+1
        m=m-1
    return fnl_lst[k-1]

def main():

    ary=[4,7,9,10]
    k=1
    print(LeetCode1060(ary,k))

    ary = [4, 7, 9, 10]
    k = 3
    print(LeetCode1060(ary,k))

    ary = [1,2,4]
    k = 3
    print(LeetCode1060(ary,k))

if __name__=='__main__':
    main()