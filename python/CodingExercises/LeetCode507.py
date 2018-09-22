'''
507. Perfect Number
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
'''

def LeetCode507(n):

    i=1
    lst=[]
    while i<n:
        rem=n%i
        if rem==0:
            lst.append(i)
        i=i+1

    sum=0
    for l in lst:
        sum=sum+l

    if sum==n:
        return True
    else:
        return False

def main():

    n=28
    print(LeetCode507(n))

if __name__=='__main__':
    main()