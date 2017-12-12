import math

def poweroftwo(n):

    if n%2!=0:
        print('Number NOT power of two')
    else:
        while n!=1:
            n=n/2
            if n%2!=0:
                break
        if n==1:
            print('Number is power of two')
        else:
            print('Number NOT power of two')


def main():
    n=128
    poweroftwo(n)

if __name__=='__main__':
    main()
