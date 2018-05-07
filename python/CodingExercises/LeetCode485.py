'''
485. Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''


def findMaxConsecutiveOnes(nums):
    max = 0
    cnt = 0
    for i in range(0, len(nums)):
        key = nums[i]
        if key == 0:
            if cnt > max:
                max = cnt
            cnt = 0
        else:
            cnt = cnt + 1
    if cnt > max:
        max = cnt
    return max

def main():
    nums=[1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(nums))

if __name__=='__main__':
    main()