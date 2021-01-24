'''
324. Wiggle Sort II
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.
'''

def LeetCode324(nums):

    for i in range(1,len(nums)):
        if i%2!=0:
            if nums[i-1]>=nums[i]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp
        else:
            if nums[i-1] <= nums[i]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp
    return nums

def main():
    
    nums = [1,5,1,1,6,4]
    print(LeetCode324(nums))

    nums = [1,3,2,2,3,1]
    print(LeetCode324(nums))

if __name__=='__main__':
    main()