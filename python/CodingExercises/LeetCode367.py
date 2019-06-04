'''
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
'''

def LeetCode367(num):

    left=1
    right=num
    while left<=right:
        mid=(left+right)//2
        square=mid*mid
        if num==square:
            return True
        elif square>num:
            right=mid-1
        else:
            left=mid+1
    return False

def main():

    num=16
    print(LeetCode367(num))

    num = 81
    print(LeetCode367(num))

    num = 14
    print(LeetCode367(num))

if __name__=='__main__':
    main()