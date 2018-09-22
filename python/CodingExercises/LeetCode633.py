'''
633. Sum of Square Numbers

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
'''

def LeetCode633(n):

    left=0
    right=n

    flg=False

    while left < right:

        tmp=left*left+right*right
        if tmp==n:
            flg=True
            break
        elif tmp>n:
            right=right-1
        elif tmp<n:
            left=left+1

    return flg

def main():
    
    n=5
    print(LeetCode633(n))

    n = 3
    print(LeetCode633(n))

if __name__=='__main__':
    main()