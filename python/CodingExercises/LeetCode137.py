'''
137. Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

def LeetCode136(ary):

    for i in range(0,len(ary)):

        key=ary[i]
        if key not in ary[:i] and key not in ary[i+1:]:
            break

    return key

def main():

    ary=[2,2,3,2]
    print(LeetCode136(ary))

    ary = [0,1,0,1,0,1,99]
    print(LeetCode136(ary))

if __name__=='__main__':
    main()