
def reversewords(str1):

    tmp=''
    st=0
    end=0
    flg=True
    tmp=''
    for i in range(len(str1)-1,-1,-1):
        if i==0 or str1[i]==' ':
            if i==0:
                st=0
            else:
                st=i+1
            flg=True
            if tmp=='':
                tmp=tmp+str1[st:end]
            else:
                tmp=tmp+' '+str1[st:end]
        else:
            if flg==True:
                end=i+1
                flg=False


    return tmp

def main():
    str1='My name is Kartik Sayee'
    print('Original String:', str1 )

    print('Reverse of the String:', reversewords(str1))

if __name__=='__main__':
    main()
