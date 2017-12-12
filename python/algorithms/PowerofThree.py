
def powerofthree(n):

    while n!=1:
        n=n/3
        if n<1:
            break
    if n==1:
        print('Number is power of 3')
    else:
        print('Number is NOT power of 3')


def main():
    n=81
    powerofthree(n)

if __name__=='__main__':
    main()
