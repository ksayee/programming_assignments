def Median(ary):

    ary.sort()

    if len(ary)%2!=0:
        n=int(len(ary)/2)
        print(ary[n])
    else:
        n=int(len(ary)/2)
        print((ary[n]+ary[n+1])/2)


def main():

    ary1 = [5, 89, 20, 64, 20, 45]

    Median(ary1)

    ary2 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]

    Median(ary2)

if __name__=='__main__':
    main()