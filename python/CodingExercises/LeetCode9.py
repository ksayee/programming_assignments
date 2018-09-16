'''
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


def LeetCode9(n):

    if n<0:
        return False
    else:

        fnl_lst=[]
        tmp=n
        while tmp!=0:
            rem=tmp%10
            fnl_lst.append(str(rem))
            tmp=int(tmp/10)

        if n==int(''.join(fnl_lst)):
            return True
        else:
            return False

def main():
    
    n=121
    print(LeetCode9(n))

    n =-121
    print(LeetCode9(n))

    n = 10
    print(LeetCode9(n))

    n = 7456547
    print(LeetCode9(n))

if __name__=='__main__':
    main()