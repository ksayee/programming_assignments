'''
941. Valid Mountain Array
Easy
Given an array A of integers, return true if and only if it is a valid mountain array.
Recall that A is a mountain array if and only if:
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Example 1:
Input: [2,1]
Output: false
Example 2:
Input: [3,5,5]
Output: false
Example 3:
Input: [0,3,2,1]
Output: true
'''

def Validate(ary):

    lst=[]

    for i in range(1,len(ary)):
        if ary[i]>=ary[i-1]:
            lst.append('I')
        else:
            lst.append('D')

    if lst[0]=='I' and lst[-1]=='D':
        return True
    else:
        return False

def LeetCode941(ary):

    if len(ary)<3:
        return False
    else:
        flg=Validate(ary)
        return flg

def main():

    ary=[2,1]
    print(LeetCode941(ary))

    ary = [3,5,5]
    print(LeetCode941(ary))

    ary=[0,3,2,1]
    print(LeetCode941(ary))

if __name__=='__main__':
    main()