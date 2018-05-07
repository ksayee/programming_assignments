def uniquedigits(num):

    dict={}

    while num!=0:
        rem=num%10
        if rem in dict.keys():
            return False
        else:
            dict[rem]=1
        num=int(num/10)

    return True

def main():

    num=45736
    print(uniquedigits(num))

    num = 1000
    print(uniquedigits(num))


if __name__=='__main__':
    main()