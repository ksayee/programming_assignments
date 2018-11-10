# Check if the brackets in the given string in balanced or not.

def ReturnGCD(num1,num2):

    if num1>num2:
        big_num=num1
        sml_num=num2
    else:
        big_num=num2
        sml_num=num1

    while big_num%sml_num!=0:
        rem=big_num%sml_num
        big_num=sml_num
        sml_num=rem
    return sml_num

def LCM(ary):

    ary.sort()

    num1=ary[0]

    for i in range(1,len(ary)):

        num2=ary[i]
        gcd=ReturnGCD(num1,num2)
        lcm=(num1*num2)/gcd
        num1=lcm
    return num1

def main():

    ary=[4, 6, 14, 10]
    print(LCM(ary))

    ary = [12,36,60]
    print(LCM(ary))

    ary = [20,28,36]
    print(LCM(ary))


if __name__=='__main__':
    main()