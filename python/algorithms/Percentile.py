def Percentile(ary,n):

    ary.sort()
    ln=len(ary)-1
    print(ary)

    for i in range(0,len(ary)):
        if (i/ln)<n:
            continue
        else:
            break
    print(ary[i])

def main():

    ary1 = [5, 89, 20, 64, 20, 45]
    n=0.75
    Percentile(ary1,n)

    ary2 = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    n=0.9
    Percentile(ary2,n)

if __name__=='__main__':
    main()