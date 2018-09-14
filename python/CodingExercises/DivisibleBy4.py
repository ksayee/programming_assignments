# Check if a large number is divisible by 4 or not
# Given a number, the task is to check if a number is divisible by 4 or not.
# The input number may be large and it may not be possible to store even if we use long long int.

def DivisibleBy4(n):

    cnt=0
    lst=[]

    while cnt<2:
        rem=n%10
        lst.append(str(rem))
        cnt=cnt+1
        n=n//10

    lst.reverse()

    if int(''.join(lst))%4==0:
        return True
    else:
        return False

def main():

    n=1124
    print(DivisibleBy4(n))

    n = 76952
    print(DivisibleBy4(n))

    n = 1234567589333862
    print(DivisibleBy4(n))

    n = 363588395960667043875487
    print(DivisibleBy4(n))

if __name__=='__main__':
    main()