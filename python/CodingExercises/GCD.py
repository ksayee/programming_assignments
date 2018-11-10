# Check if the brackets in the given string in balanced or not.

def ReturnGCD(sml_num,big_num):

    while big_num%sml_num!=0:
        rem=big_num%sml_num
        big_num=sml_num
        sml_num=rem
    return sml_num

def GCD(ary):

    ary.sort()

    sml_num=ary[0]

    for i in range(1,len(ary)):

        big_num=ary[i]
        sml_num=ReturnGCD(sml_num,big_num)
    return sml_num

def main():

    ary=[4, 6, 14, 10]
    print(GCD(ary))

    ary = [12,36,60]
    print(GCD(ary))

    ary = [20,28,36]
    print(GCD(ary))


if __name__=='__main__':
    main()