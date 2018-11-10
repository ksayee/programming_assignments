# Give the fist 20 Fibonaci Series.

def FibonaciSeries(n):

    fnl_lst=[]
    fnl_lst.append(0)
    fnl_lst.append(1)
    k=2

    while k<=20:
        sum=fnl_lst[k-1]+fnl_lst[k-2]
        fnl_lst.append(sum)
        k=k+1
    return fnl_lst
def main():

    n = 20
    print(FibonaciSeries(n))

if __name__=='__main__':
    main()