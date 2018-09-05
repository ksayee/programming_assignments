# Total numbers with no repeated digits in a range
# Given a range L,R find total such numbers in the the given range such that they have no repeated digits.

def Factorial(n):

    if n==1:
        return 1
    res=n*Factorial(n-1)
    return res

def main():

    n=5
    print(Factorial(n))

if __name__=='__main__':
    main()