
def reversenumber(num):

    lst=[]

    while num!=0:
        lst.append(str(num%10))
        num=int(num/10)


    print(int(''.join(lst)))



def main():

    num=8745
    reversenumber(num)

    num = 9830
    reversenumber(num)


if __name__=='__main__':
    main()
