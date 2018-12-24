'''
# Given a number as input write a function that returns a
# string with binary representation of a positive integer number
# We would like you to write the algorithm to generate this
# binary representation in string format without library functions

def to_bin(n):
    # write your code here
    return bin_str

# Sample test cases to verify functionality
assert to_bin(2) == '10'
assert to_bin(7) == '111'
assert to_bin(45) == '101101'
assert to_bin(32) == '100000'
assert to_bin(0) == '0'
'''

def IntegerToBinary(n):

    fnl_lst=[]

    if n==0:
        fnl_lst.append(str(0))
    while n!=0:
        rem=n%2
        fnl_lst.append(str(rem))
        n=int(n/2)
    fnl_lst.reverse()
    return int(''.join(fnl_lst))

def main():

    n=2
    print(IntegerToBinary(n))

    n = 7
    print(IntegerToBinary(n))

    n = 45
    print(IntegerToBinary(n))

    n = 32
    print(IntegerToBinary(n))

    n = 0
    print(IntegerToBinary(n))

if __name__=='__main__':
    main()