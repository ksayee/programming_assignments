# This is question from Cracking the coding interview. Chapter 1.6

def stringcompression(str1):

    prev_chr=''
    tmp=''
    cnt=0
    for i in range(0,len(str1)):
       if prev_chr!=str1[i]:
           if prev_chr!='':
               tmp=tmp+prev_chr+str(cnt)
               prev_chr=str1[i]
           else:
               prev_chr = str1[i]
           cnt=1
       else:
           cnt=cnt+1
    tmp=tmp+str1[i]+str(cnt)
    return tmp

def stringexpansion(str1):

    prev_chr=''
    tmp=''
    for i in range(0,len(str1)):
        if (ord(str1[i])>=65 and ord(str1[i])<=90) or (ord(str1[i])>=97 and ord(str1[i])<=122):
            prev_chr=str1[i]

        else:
            j = 0
            while (j < int(str1[i])):
                tmp = tmp + prev_chr
                j = j + 1

    return tmp
def main():
    str1 = 'aabcccccaa'

    print('Compressed String:',stringcompression(str1))
    print('Expaned String:',stringexpansion(stringcompression(str1)))

if __name__=='__main__':
    main()
