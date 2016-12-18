def uniquedigits(num):

    fnl_lst=[]
    for i in range(0,num):
        lst={}

        if i>9:
            n=i
            found=False
            unq_flg=True
            while n!=0:
                key=n%10
                if key in lst.keys() and found==True:
                    lst[key]=lst.get(key)+1
                elif found==False:
                    lst[key]=1
                    found=True
                else:
                    unq_flg=False
                    break
                n=int(n/10)

            if unq_flg==True:
                fnl_lst.append(i)

    print(fnl_lst)

def main():

    num=100
    uniquedigits(num)

if __name__=='__main__':
    main()
