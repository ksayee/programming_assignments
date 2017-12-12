# This is question from Cracking the coding interview. Chapter 1.9

def segmentsstring(str1):

    cnt=0
    flg=0
    for i in range(0,len(str1)):
        if flg==0 and (str1[i]>='a' and str1[i]<='z') or (str1[i]>='A' and str1[i]<='Z'):
            flg=1
            cnt=cnt+1
        elif str1[i]==' ':
            flg=0
        else:
            continue

    print(cnt)



def main():
    str1 = '     Hello my       name is Kartik     '

    segmentsstring(str1)



if __name__=='__main__':
    main()
