def missingwords(str1,str2):

    lst={}
    st=0
    end=0
    flg=True

    for i in range(0,len(str1)):
        if str1[i]==' ' or i+1==len(str1):
            if i+1==len(str1):
                end=i+1
            else:
                end=i
            key=str1[st:end]

            if key in lst.keys():
                lst[key]=lst.get(key)+1
            else:
                lst[key]=1
            flg=True
        else:
            if flg==True:
                st=i
                flg=False

    for key,val in lst.items():
        print(key,val)

    st=0
    end=0
    flg=True

    print('Below are the number of words NOT existing in:')
    for i in range(0,len(str2)):
        if str2[i]==' ' or i+1==len(str2):
            if i+1==len(str2):
                end=i+1
            else:
                end=i
            key=str2[st:end]
            flg=True
            if key not in lst.keys():
                print(key)
        else:
            if flg==True:
                st=i
                flg=False

def main():
    str1 = 'Life is beautiful and not fair in real world'
    str2 = 'beautiful and white world is san francisco'

    missingwords(str1,str2)

if __name__=='__main__':
    main()
