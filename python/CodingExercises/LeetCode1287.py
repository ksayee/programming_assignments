'''
1287. Element Appearing More Than 25% In Sorted Array
Easy
Given an integer array sorted in non-decreasing order,
there is exactly one integer in the array that occurs more than 25% of the time.
Return that integer.
Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
'''

import collections

def LeetCode1287(ary):

    dict=collections.Counter(ary)
    length=len(ary)
    for key,val in dict.items():
        if val/length>=0.25:
            return key
    return 'No Item'
        
def main():

    ary=[1,2,2,6,6,6,6,7,10]
    print(LeetCode1287(ary))

if __name__=='__main__':
    main()