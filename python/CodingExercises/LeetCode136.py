'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

def LeetCode136(ary):

    for i in range(0,len(ary)):
        key=ary[i]

        if key not in ary[i+1:] and key not in ary[:i]:
           break

    return key

def main():

    ary=[2,2,1]
    print(LeetCode136(ary))

    ary = [4,1,2,1,2]
    print(LeetCode136(ary))

if __name__=='__main__':
    main()