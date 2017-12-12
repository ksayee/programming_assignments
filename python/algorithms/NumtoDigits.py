def NumtoDigits(num):

    fnl=[]

    while num!=0:
        fnl.append(str(num%10))
        num=int(num/10)

    fnl.reverse()

    print(fnl)


def main():

    num=123
    NumtoDigits(num)

    num = 400
    NumtoDigits(num)

if __name__=='__main__':
    main()