def CountLetters(str1):

    cnt=0
    for i in range(0,len(str1)):
        if (str1[i]>='a' and str1[i]<='z') or (str1[i]>='A' and str1[i]<='Z'):
            cnt=cnt+1

    print(cnt)

def main():

    str1 = 'I work in Amazon in Seattle'
    str2 = '    I    work * * %    in    Amazon     in Seattle'
    str3 = '*%I     work in    Amazon in     Seattle   $    '

    CountLetters(str1)
    CountLetters(str2)
    CountLetters(str3)

if __name__=='__main__':
    main()