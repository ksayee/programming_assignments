'''
263. Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
'''

def LeetCode263(lst,n):

    i=2
    tmp=[]
    while i<n:
        if n%i==0:
            tmp.append(i)
        i=i+1

    flg=True
    for key in tmp:
        if key not in lst:
            found=False
            for num in tmp:
                if num<key and key%num==0:
                    found=True
                    break
            flg=found

    return flg

def main():

    lst=[2,3,5]
    n=6
    print(LeetCode263(lst,n))

    n = 8
    print(LeetCode263(lst,n))

    n = 14
    print(LeetCode263(lst,n))


if __name__=='__main__':
    main()