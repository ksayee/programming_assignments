'''
33. Search in Rotated Sorted Array
You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1
'''

def LeetCode33(nums,target):

    left =0
    right = len(nums)-1

    while left <=right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid -1
            else:
                left = mid +1
        else:
            if target <= nums[right] and target>=nums[mid]:
                left = mid +1
            else:
                right = mid -1
    return -1

def main():

    nums = [4,5,6,7,0,1,2]
    target = 0
    print(LeetCode33(nums,target))

    nums = [4,5,6,7,0,1,2]
    target = 3
    print(LeetCode33(nums, target))

    nums = [1]
    target = 0
    print(LeetCode33(nums, target))

if __name__=='__main__':
    main()