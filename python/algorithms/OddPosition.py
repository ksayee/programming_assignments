def OddPosition(ary):

    fnl=[]

    for i in range(0,len(ary)):
        if i%2!=0:
            fnl.append(ary[i])
    print(fnl)


def main():

    ary=[0,1,2,3,4,5]
    OddPosition(ary)

    ary = [1,-1,2,-2]
    OddPosition(ary)


if __name__=='__main__':
    main()