# Total numbers with no repeated digits in a range
# Given a range L,R find total such numbers in the the given range such that they have no repeated digits.

def NoRepeatedDigits(l,r):

    fnl_lst=[]

    while l<=r:
        num=l
        tmp=[]
        flg=True
        while num!=0:
            rem=num%10
            if rem not in tmp:
                tmp.append(rem)
            else:
                flg=False
                break
            num=int(num/10)
        if flg==True:
            fnl_lst.append(l)
        l=l+1

    return len(fnl_lst)

def main():

    l=10
    r=12
    print(NoRepeatedDigits(l,r))

    l = 1
    r = 100
    print(NoRepeatedDigits(l, r))

if __name__=='__main__':
    main()