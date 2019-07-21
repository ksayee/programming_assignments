'''
852. Peak Index in a Mountain Array
Easy
Let's call an array A a mountain if the following properties hold:
A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
Example 1:
Input: [0,1,0]
Output: 1
Example 2:
Input: [0,2,1,0]
Output: 1
'''

def CheckMountain(ary):

    lst=[]
    for i in range(1,len(ary)):
        if ary[i]>ary[i-1]:
            lst.append('I')
        else:
            lst.append('D')

    if lst[0]=='I' and lst[-1]=='D':
        return True
    else:
        return False
def LeetCode852(ary):

    flg=CheckMountain(ary)
    if flg==True:
        max=-999
        idx=-9
        for i in range(0,len(ary)):
            if ary[i]>max:
                max=ary[i]
                idx=i
        return idx
    else:
        return -1

def main():

    ary=[0,1,0]
    print(LeetCode852(ary))

    ary = [0,2,1,0]
    print(LeetCode852(ary))

if __name__=='__main__':
    main()