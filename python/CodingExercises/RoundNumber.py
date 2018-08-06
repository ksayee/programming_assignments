# Round the given number to nearest multiple of 10
# Given a positive integer n, round it to nearest whole number having zero as last digit.

def RoundNumber(n):

    rem=n%10
    print("Original Number:",n)
    if rem<5:
        num=n-rem
    else:
        num=n+(10-rem)

    return num

def main():

    n=4722
    print("New Number:",RoundNumber(n))

    n = 38
    print("New Number:",RoundNumber(n))

    n = 10
    print("New Number:",RoundNumber(n))

if __name__=='__main__':
    main()