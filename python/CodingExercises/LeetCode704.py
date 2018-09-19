'''
704. Binary Search
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''


def LeetCode186(ary,k):

    left=0
    right=len(ary)-1

    idx=-1
    while left<right:

        mid=int((left+right)/2)
        if k==ary[mid]:
            idx=mid
            break
        elif k<ary[mid]:
            right=mid-1
        elif k>ary[mid]:
            left=mid+1

    return idx

def main():

    ary=[-1,0,3,5,9,12]
    k=9
    print(LeetCode186(ary,k))

    ary = [-1, 0, 3, 5, 9, 12]
    k = 2
    print(LeetCode186(ary, k))

if __name__=='__main__':
    main()