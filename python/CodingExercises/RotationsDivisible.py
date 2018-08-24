def RotationsDivisible(n):

    lst=list(str(n))

    fnl_lst=[]
    for i in range(0,len(lst)):

        tmp=''.join(lst[i:])+''.join(lst[0:i])

        num=int(tmp)
        if num%4==0:
            fnl_lst.append(str(num))

    if len(fnl_lst)>0:
        return fnl_lst
    else:
        return "No Rotations Divisible"

def main():

    n=8
    print(RotationsDivisible(n))

    n = 20
    print(RotationsDivisible(n))

    n=13502
    print(RotationsDivisible(n))

    n = 43292816
    print(RotationsDivisible(n))


if __name__=='__main__':
    main()