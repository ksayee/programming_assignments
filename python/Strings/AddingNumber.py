#Program to add a single number until we reach single digit
#eg: 38: 3+8=11: 1+1=2
def addnum(n):

    flg=True
    sum=0
    while flg==True:
        sum=0
        while n!=0:
            sum=sum+(n%10)
            n=int(n/10)
        if sum<10:
            flg=False
        else:
            n=sum
    return sum


def main():
    num=679
    print('Sum of number:',addnum(num))

if __name__=='__main__':
    main()