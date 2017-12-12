def StringExpansion(str1):

    cnt=0
    tmp=''
    for i in range(0,len(str1)):
        if ord(str1[i])>=48 and ord(str1[i])<=57:
            cnt=int(str1[i])
            while cnt!=0:
                if tmp=='':
                    tmp=prev_char
                else:
                    tmp=tmp+prev_char
                cnt=cnt-1
        prev_char=str1[i]

    print(tmp)

def main():

    str1 = 'a3b1c5a2'

    StringExpansion(str1)

if __name__=='__main__':
    main()