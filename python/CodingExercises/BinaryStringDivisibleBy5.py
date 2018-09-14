# Decimal representation of given binary string is divisible by 5 or not
# The problem is to check whether the decimal representation of the given binary number is divisible by 5 or not.
# Take care, the number could be very large and may not fit even in long long int.
# The approach should be such that there are zero or minimum number of multiplication and division operations.
# No leading 0’s are there in the input.
'''
Approach: The following steps are:

Convert the binary number to base 4.
Numbers in base 4 contains only 0, 1, 2, 3 as their digits.
5 in base 4 is equivalent to 11.
Now apply the rule of divisibility by 11 where you add all the digits at odd places and add all the digits at even places and then subtract one from the other. If the result is divisible by 11(which remember is 5), then the binary number is divisible by 5.
How to covert binary number to base 4 representation?

Check whether the length of binary string is even or odd.
If odd, the add ‘0’ in the beginning of the string.
Now, traverse the string from left to right.
One by extract substrings of size 2 and add their equivalent decimal to the resultant string.
'''

def ConvertToBase4(str1):

    if str1=='00':
        return 0
    if str1 == '01':
        return 1
    if str1 == '10':
        return 2
    return 3

def DivibleBy11(num):

    lst=list(num)
    odd_sum=0
    even_sum=0

    for i in range(0,len(lst)):

        if i%2!=0:
            odd_sum=odd_sum+int(lst[i])
        else:
            even_sum=even_sum+int(lst[i])

    if int(odd_sum-even_sum)%11==0:
        return True
    else:
        return False

def BinaryStringDivisibleBy5(n):

    lst=[]

    if len(str(n))%2!=0:
        lst.append('0')
        tmp=list(str(n))
        lst.extend(tmp)
    else:
        lst=list(str(n))

    i=0
    j=2
    fnl_lst=[]
    while j<=len(lst):
        tmp=lst[i:j]
        num=ConvertToBase4(''.join(tmp))
        fnl_lst.append(str(num))
        i=i+2
        j=j+2

    flg=DivibleBy11(''.join(fnl_lst))
    return flg

def main():

    n=1010
    print(BinaryStringDivisibleBy5(n))

    n = 10000101001
    print(BinaryStringDivisibleBy5(n))

if __name__=='__main__':
    main()