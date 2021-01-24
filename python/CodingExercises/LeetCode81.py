'''
81. Search in Rotated Sorted Array II
You are given an integer array nums sorted in ascending order (not necessarily distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,4,4,5,6,6,7] might become [4,5,6,6,7,0,1,2,4,4]).
If target is found in the array return its index, otherwise, return -1.
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''

def LeetCode81(nums,target):

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return True
        elif nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid -1
            else:
                left = mid +1
        else:
            if target >= nums[mid] and  target <= nums[right]:
                left = mid +1
            else:
                right = mid -1
    return False

def main():
    
    nums = [2,5,6,0,0,1,2]
    target = 0
    print(LeetCode81(nums,target))

    nums = [2,5,6,0,0,1,2]
    target = 3
    print(LeetCode81(nums, target))

if __name__=='__main__':
    main()