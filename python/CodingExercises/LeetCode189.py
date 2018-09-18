'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

def LeetCode189(ary,k):

    while k>len(ary):
        k=k-len(ary)

    return ary[-k:]+ary[:len(ary)-k]

def main():

    ary=[1,2,3,4,5,6,7]
    k=3
    print(LeetCode189(ary,k))

    ary = [-1,-100,3,99]
    k = 2
    print(LeetCode189(ary, k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k =5
    print(LeetCode189(ary, k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k = 6
    print(LeetCode189(ary, k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k = 7
    print(LeetCode189(ary, k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k = 10
    print(LeetCode189(ary, k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k = 15
    print(LeetCode189(ary, k))

    ary = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    print(LeetCode189(ary, k))

if __name__=='__main__':
    main()