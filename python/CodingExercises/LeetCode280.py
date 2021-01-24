'''
280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
'''

def LeetCode280(nums):

    for i in range(1,len(nums)):
        if i%2!=0:
            if nums[i-1]>nums[i]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp
        else:
            if nums[i-1] < nums[i]:
                tmp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = tmp
    return nums


def main():
    
    nums = [3, 5, 2, 1, 6, 4]
    print(LeetCode280(nums))

if __name__=='__main__':
    main()