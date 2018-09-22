'''
724. Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
'''

def LeetCode724(ary):

    left_sum=0
    right_sum=0

    n=len(ary)-1
    flg=False
    for i in range(1,len(ary)-1):

        left_sum=left_sum+ary[i-1]
        if right_sum==left_sum:
            flg=True
            break
        else:
            while right_sum<left_sum:
                right_sum=right_sum+ary[n]
                if left_sum==right_sum:
                    flg=True
                    break
                n=n-1

    if flg==False:
        return -1
    else:
        return i

def main():

    ary=[1, 7, 3, 6, 5, 6]
    print(LeetCode724(ary))

    ary = [1, 2, 3]
    print(LeetCode724(ary))

if __name__=='__main__':
    main()