'''
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

def LeetCode283(ary):

    k=0
    for i in range(0,len(ary)):
        if ary[i]!=0:
            ary[k]=ary[i]
            k=k+1

    while k<len(ary):
        ary[k]=0
        k=k+1

    return ary


def main():

    ary=[0,1,0,3,12]
    print(LeetCode283(ary))

    ary=[1, 2, 0, 4, 3, 0, 5, 0]
    print(LeetCode283(ary))

if __name__=='__main__':
    main()