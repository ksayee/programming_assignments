'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
'''


def LeetCode162(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):

        if i==0:
            if ary[i]>ary[i+1]:
                fnl_lst.append(i)
        elif i==len(ary)-1:
            if ary[i]>ary[i-1]:
                fnl_lst.append(i)
        else:
            if ary[i]>ary[i+1] and ary[i]>ary[i-1]:
                fnl_lst.append(i)

    return fnl_lst


def main():

    ary=[1,2,3,1]
    print(LeetCode162(ary))

    ary = [1,2,1,3,5,6,4]
    print(LeetCode162(ary))

if __name__=='__main__':
    main()