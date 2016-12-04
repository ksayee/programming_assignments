def multiply(ary):

    left=[1]*len(ary)
    right=[1]*len(ary)
    prod=[1]*len(ary)

    for i in range(1,len(ary)):
        left[i]=ary[i-1]*left[i-1]

    for i in range(len(ary)-2,-1,-1):
        right[i]=ary[i+1]*right[i+1]

    for i in range(0,len(ary)):
        prod[i]=left[i]*right[i]

    print(prod)


def main():

    ary=[1,2,3,4]
    multiply(ary)

if __name__=='__main__':
    main()
