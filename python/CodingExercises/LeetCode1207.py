'''
1207. Unique Number of Occurrences
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.
Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
Input: arr = [1,2]
Output: false
Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

import collections
def LeetCode1207(lst):

    dict=collections.Counter(lst)

    rev_dict={}

    for key,val in dict.items():
        if val not in rev_dict.keys():
            rev_dict[val]=[]
            rev_dict[val].append(key)
        else:
            return False
    return True

def main():

    lst=[1,2,2,1,1,3]
    print(LeetCode1207(lst))

    lst = [1,2]
    print(LeetCode1207(lst))

    lst = [-3,0,1,-3,1,1,1,-3,10,0]
    print(LeetCode1207(lst))

if __name__=='__main__':
    main()