'''
747. Largest Number At Least Twice of Others
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.
Example 1:
Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
Example 2:
Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
'''

def LeetCode747(nums):

    sort_list=sorted(nums)
    max_num=sort_list[-1]

    for i in range(0,len(sort_list)-1):
        key=sort_list[i]
        if max_num>=key*2:
            pass
        else:
            return -1
    return nums.index(max_num)

def main():

    nums = [3, 6, 1, 0]
    print(LeetCode747(nums))

    nums = [1, 2, 3, 4]
    print(LeetCode747(nums))

if __name__=='__main__':
    main()