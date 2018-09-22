'''
665. Non-decreasing Array
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
'''

def LeetCode665(ary):

    cnt=0
    for i in range(0,len(ary)-1):

        if ary[i]<=ary[i+1]:
            continue
        else:
            cnt=cnt+1

    if cnt==1:
        return True
    else:
        return False

def main():

    ary=[4,2,3]
    print(LeetCode665(ary))

    ary = [4,2,1]
    print(LeetCode665(ary))

if __name__=='__main__':
    main()