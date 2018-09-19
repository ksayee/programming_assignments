'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
'''

def Factorial(n):

    if n==0:
        return 1
    return n*Factorial(n-1)

def LeetCode172(n):

    num=Factorial(n)

    found=False
    cnt=0
    while found!=True:

        rem=num%10
        if rem==0:
            if found==False:
                cnt=cnt+1
        else:
            found=True
        num=num//10

    return cnt

def main():

    n=3
    print(LeetCode172(n))

    n = 5
    print(LeetCode172(n))


if __name__=='__main__':
    main()