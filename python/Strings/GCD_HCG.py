def gcd_hcf(ary):

    gcd=0

    for i in range(0,len(ary)):
        if i==0:
            num1 = ary[i]
            num2 = ary[i + 1]
        elif i==1:
            continue
        else:
            num1=gcd
            num2=ary[i]

        if num1<num2:
            small=num1
            large=num2
        else:
            small=num2
            large=num1

        while True:
            if large%small!=0:
                tmp=small
                small = large%small
                large = tmp
            else:
                gcd=small
                break

    print(gcd)

def main():
    ary=[54,108,144]

    gcd_hcf(ary)

if __name__=='__main__':
    main()
