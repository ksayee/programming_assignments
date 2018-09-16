'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''

def LeetCode35(ary,n):

    l=0
    r=len(ary)-1

    found=False
    while l<r:

        mid=int((l+r)/2)

        if n==ary[mid]:
            found=True
            break
        elif n>ary[mid]:
            l=mid+1
        else:
            r=mid-1

    if found==True:
        idx=mid
    elif found==False and l==r:
        if n<ary[l]:
            idx=l
        else:
            idx=l+1

    return idx

def main():
    
    ary=[1,3,5,6]
    n=5
    print(LeetCode35(ary,n))

    ary = [1,3,5,6]
    n = 2
    print(LeetCode35(ary, n))

    ary = [1,3,5,6]
    n = 7
    print(LeetCode35(ary, n))

    ary = [1,3,5,6]
    n = 0
    print(LeetCode35(ary, n))

if __name__=='__main__':
    main()