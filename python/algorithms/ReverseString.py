def ReverseString(str1):

    st=0
    end=0
    fnl_str=''
    flg=True

    for i in range(len(str1)-1,-1,-1):
        if str1[i]==' ' or i==0:
            if i==0:
                st=0
            else:
                st=i+1
            key=str1[st:end]
            if fnl_str=='':
                fnl_str=key
            else:
                fnl_str=fnl_str+' '+key
            flg=True
        else:
            if flg==True:
                end=i+1
                flg=False

    print(fnl_str)

def main():

    str1='I am using hackerrank to improve programming'
    ReverseString(str1)

if __name__=='__main__':
    main()