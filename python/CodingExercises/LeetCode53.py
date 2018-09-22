'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

def LeetCode53(ary):

    lst=[0]*len(ary)

    sum=0
    for i in range(0,len(ary)):
        sum=sum+ary[i]
        lst[i]=sum

    max=-999
    idx=-1
    for i in range(0,len(lst)):
        if lst[i]>max:
            max=lst[i]
            idx=i

    for i in range(1,idx):
        if lst[i]>lst[i-1]:
            continue
        else:
            break
    return ary[i+1:idx+1]

def main():

    ary=[-2,1,-3,4,-1,2,1,-5,4]
    print(LeetCode53(ary))

    ary = [1, -2, 1, 1, -2, 1]
    print(LeetCode53(ary))

    ary = [-2, 7, -6, -1, 5, 6, -3]
    print(LeetCode53(ary))

    ary=[-2, -3, 4, -1, -2, 1, 5, -3]
    print(LeetCode53(ary))

if __name__=='__main__':
    main()