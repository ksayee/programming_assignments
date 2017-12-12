def Str1Str2Comp(str1,str2):

    lst={}

    st=0
    end=0
    flg=True
    for i in range(0,len(str2)):
        if str2[i]==' ' or i+1==len(str2):

            if i+1==len(str2):
                end=i+1
            else:
                end=i

            key=str2[st:end]
            if key in lst.keys():
                lst[key]=lst.get(key)+1
            else:
                lst[key]=1
            flg=True

        else:
            if flg==True:
                st=i
                flg=False

    st=0
    end=0
    flg=True
    fnl=[]
    for i in range(0,len(str1)):
        if str1[i]==' ' or i+1==len(str1):
            if i+1==len(str1):
                end=i+1
            else:
                end=i
            key=str1[st:end]
            if key not in lst.keys():
                fnl.append(key)
            flg=True
        else:
            if flg==True:
                st=i
                flg=False

    print(fnl)

def main():

    str1='I am using hackerrank to improve programming'
    str2 ='am hackerrank to improve'
    Str1Str2Comp(str1,str2)

if __name__=='__main__':
    main()