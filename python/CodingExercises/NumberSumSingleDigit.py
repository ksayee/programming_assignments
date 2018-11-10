# Given the sum of number in single digit.

def NumberSum(n):

    while n>9:
        sum=0
        while n!=0:
            rem=n%10
            sum=sum+rem
            n=n//10
        n=sum
    return n
def main():

    n = 679
    print(NumberSum(n))

if __name__=='__main__':
    main()