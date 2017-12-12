def cumulativeSum(ary):

    fnl = []
    sum = 0

    for i in range(0, len(ary)):
        sum = sum + ary[i]
        fnl.append(sum)
    print(fnl)

def main():

    ary=[1,1,1]
    cumulativeSum(ary)

    ary = [1,-1,3]
    cumulativeSum(ary)


if __name__=='__main__':
    main()