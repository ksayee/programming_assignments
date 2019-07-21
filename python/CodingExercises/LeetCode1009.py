'''
1009. Complement of Base 10 Integer
Easy
Every non-negative integer N has a binary representation.
 For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.
The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.
For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.
Example 1:
Input: 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:
Input: 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:
Input: 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
'''

def GetBinary(num):

    lst=[]
    while num!=0:
        rem=num%2
        num=num//2
        lst.append(str(rem))
    lst.reverse()
    return ''.join(lst)

def GetComplement(bin_num):

    lst=[]
    for i in range(0,len(bin_num)):
        if bin_num[i]=='0':
            lst.append(1)
        else:
            lst.append(0)
    return lst

def LeetCode1009(num):

    bin_num=GetBinary(num)
    com_num=GetComplement(bin_num)

    sum=0
    k=0
    for i in range(len(com_num)-1,-1,-1):
        sum=sum+(com_num[i]*(2**k))
        k=k+1
    return sum

def main():

    num=5
    print(LeetCode1009(num))

    num = 7
    print(LeetCode1009(num))

    num = 10
    print(LeetCode1009(num))

if __name__=='__main__':
    main()