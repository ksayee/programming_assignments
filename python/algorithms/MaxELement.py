def findmax(ary):

    for i in range(0,len(ary)):
        if i==0:
            max=ary[i]

        else:
            if ary[i]>max:
                max=ary[i]
    return max

def main():
    ary=[5,89,20,64,20,45,]

    print('Maximum Element:', findmax(ary))

if __name__=='__main__':
    main()
