
def searchinsert(ary,n):

    flg=0
    for i in range(0,len(ary)):
        if ary[i]==n:
            print('Position is:',i)
            flg=1
            break
        elif ary[i]<n:
            continue
        else:
            print('Insert position is:', i)
            flg=1
            break

    if flg==0:
        print('Insert position is:',i+1)


def main():

    ary=[1,3,5,6]
    n=5
    searchinsert(ary,n)

    ary = [1, 3, 5, 6]
    n = 2
    searchinsert(ary, n)

    ary=[1,3,5,6]
    n=7
    searchinsert(ary,n)

    ary=[1,3,5,6]
    n=0
    searchinsert(ary,n)


if __name__=='__main__':
    main()
