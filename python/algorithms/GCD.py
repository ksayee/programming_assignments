def computeGCD(small,big):

    while small%big!=0:
        rem=small%big
        big=small
        small=rem

    return small

def GCD(ary):

    ary.sort()
    small=ary[0]
    big=ary[1]

    gcd=computeGCD(small,big)

    for i in range(2,len(ary)):
        gcd=computeGCD(gcd,ary[i])

    print(gcd)


def main():
    ary = [54,108,144]
    GCD(ary)

if __name__=='__main__':
    main()