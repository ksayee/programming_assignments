'''
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''


def majorityElement(nums):
    dict = {}

    for i in range(0, len(nums)):
        key = nums[i]
        if key in dict.keys():
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1

    for key, val in dict.items():
        if val > int(len(nums) / 2):
            return key

def main():
    nums=[3,2,3]
    print(majorityElement(nums))

    nums = [2,2,1,1,1,2,2]
    print(majorityElement(nums))

if __name__=='__main__':
    main()