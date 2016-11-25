# This is question from Cracking the coding interview. Chapter 1.3

def replacespaces(str1):

    tmp=''
    st_chr=0
    spc_flg=0
    for i in range(0,len(str1)):
        if str1[i]!='$':
            if st_chr==0:
                st_chr=1
            if spc_flg==1:
                tmp=tmp+'02%'+str1[i]
                spc_flg=0
            else:
                tmp=tmp+str1[i]
        else:
            if st_chr==0:
                continue
            else:
                spc_flg=1
    return tmp

def main():
    str1 = '$$$$$Mr$$John$Smith$$$$$$'
    str2 = 'Mr$$John$Smith'
    str3 = '$$$$$Mr$$John$Smith'
    str4 = '$$$$$Mr$$John$$$$Smith$'

    print('Output is:', replacespaces(str1))
    print('Output is:', replacespaces(str2))
    print('Output is:', replacespaces(str3))
    print('Output is:', replacespaces(str4))

if __name__=='__main__':
    main()
