'''
303. Range Sum Query - Immutable
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
'''

def LeetCode303(ary,i,j):

    sum=0
    while i<=j:
        sum=sum+ary[i]
        i=i+1

    return sum

def main():

    ary=[-2, 0, 3, -5, 2, -1]
    print(LeetCode303(ary,0,2))
    print(LeetCode303(ary, 2, 5))
    print(LeetCode303(ary, 0, 5))

if __name__=='__main__':
    main()