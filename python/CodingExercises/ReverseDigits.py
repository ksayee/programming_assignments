def ReverseDigits(n):

    fnl_lst=[]

    neg_flg=False
    if n<0:
        neg_flg=True
        n=(-1)*n

    found=False
    while n!=0:
        rem=n%10
        if n==0 and found==False:
            n=n//10
        else:
            fnl_lst.append(str(rem))
            n=n//10

    if neg_flg==True:
        return int(''.join(fnl_lst))*(-1)
    else:
        return int(''.join(fnl_lst))

def main():

    n=123
    print(ReverseDigits(n))

    n = -123
    print(ReverseDigits(n))

    n = 1200
    print(ReverseDigits(n))

    n = 5640098
    print(ReverseDigits(n))

    n = 564009800
    print(ReverseDigits(n))

if __name__=='__main__':
    main()