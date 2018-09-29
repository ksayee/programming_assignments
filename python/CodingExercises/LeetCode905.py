'''
905. Sort Array By Parity
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
You may return any answer array that satisfies this condition.
Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

def LeetCode905(ary):

    tmp=[0]*len(ary)

    odd=len(ary)-1
    even=0

    for i in range(0,len(ary)):
        key=ary[i]
        if key%2==0:
            tmp[even]=key
            even=even+1
        else:
            tmp[odd]=key
            odd=odd-1

    return tmp

def main():

    ary=[3,1,2,4]
    print(LeetCode905(ary))

if __name__=='__main__':
    main()