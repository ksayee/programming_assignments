'''
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

def LeetCode202(n):

    while n>=10:
        tmp=n
        sum=0
        while tmp!=0:
            rem=tmp%10
            sum=sum+rem*rem
            tmp=int(tmp/10)
        n=sum
    if n==1:
        return True
    else:
        return False

def main():

    n=19
    print(LeetCode202(n))

    n = 622
    print(LeetCode202(n))

    n = 208
    print(LeetCode202(n))

    n = 200
    print(LeetCode202(n))

if __name__=='__main__':
    main()