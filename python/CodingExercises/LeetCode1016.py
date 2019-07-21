'''
1016. Binary String With Substrings Representing 1 To N
Medium
Given a binary string S (a string consisting only of '0' and '1's) and a
positive integer N, return true if and only if for every integer X from 1 to N, the
binary representation of X is a substring of S.
Example 1:
Input: S = "0110", N = 3
Output: true
Example 2:
Input: S = "0110", N = 4
Output: false
'''

def GetBinary(num):

    tmp=[]
    while num!=0:
        rem=num%2
        tmp.append(str(rem))
        num=num//2
    tmp.reverse()
    return ''.join(tmp)

def LeetCode1016(bin_string, n):

    lst=[]
    i=1
    while i<=n:
        lst.append(i)
        i=i+1
    bin_lst=[]
    for num in lst:
        bin_num=GetBinary(num)
        bin_lst.append(bin_num)

    for bin_num in bin_lst:
        try:
            idx=bin_string.index(bin_num)
        except:
            return False
    return True

def main():

    bin_string='0110'
    n=3
    print(LeetCode1016(bin_string,n))

    bin_string = '0110'
    n = 4
    print(LeetCode1016(bin_string, n))

if __name__=='__main__':
    main()