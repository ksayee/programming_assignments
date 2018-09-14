# Check if a large number is divisible by 11 or not
# Given a number, the task is to check if the number is divisible by 11 or not.
# The input number may be large and it may not be possible to store it even if we use long long int.

def DivisibleBy11(n):

    lst=list(str(n))

    odd_sum=0
    even_sum=0
    for i in range(0,len(lst)):

        if i%2!=0:
            odd_sum=odd_sum+int(lst[i])
        else:
            even_sum=even_sum+int(lst[i])

    if (odd_sum-even_sum)%11==0:
        return True
    else:
        return False

def main():

    n=76945
    print(DivisibleBy11(n))

    n = 1234567589333892
    print(DivisibleBy11(n))

    n = 363588395960667043875487
    print(DivisibleBy11(n))

if __name__=='__main__':
    main()