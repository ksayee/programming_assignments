def wordcount(str1):

    st=0
    end=0
    prev_letter=' '
    flg=True
    lst={}
    for i in range(0,len(str1)):
        if str1[i]==' ' or i+1==len(str1):

            if(i+1==len(str1)):
                end=i+1
            else:
                end=i
            flg=True
            key=str1[st:end]
            if key in lst.keys():
                lst[key]=lst.get(key)+1
            else:
                lst[key]=1
        else:
            if flg==True:
                st=i
                flg=False
            prev_letter=str1[i]

    for key,val in lst.items():
        print(key,val)


def main():
    str1 = 'I work in Amazon in Seattle I life'

    wordcount(str1)

if __name__=='__main__':
    main()
