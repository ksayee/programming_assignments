# Rearrange a list such that even and odd elements are seperated each end of the list

def RearrangeAryEvenOddEachEnd(ary):

    odd=len(ary)-1
    i=0
    while i<odd:
        if ary[i]%2!=0:
            tmp=ary[odd]
            ary[odd]=ary[i]
            ary[i]=tmp
            odd=odd-1
        else:
            i=i+1
    return ary

def main():

    ary=[5,3,4,2,6,11,13,22,8,6]
    print(RearrangeAryEvenOddEachEnd(ary))

if __name__=='__main__':
    main()