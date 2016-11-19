def lettercount(str1):

    count=0
    for i in range(0,len(str1)):
        if (str1[i]>='a' and str1[i]<='z') or (str1[i]>='A' and str1[i]<='Z'):
            count=count+1
    return count

def main():
    str1 = 'I work in Amazon in Seattle'
    str2 = '    I    work * * %    in    Amazon     in Seattle'
    str3 = '*%I     work in    Amazon in     Seattle   $    '

    print("Count of letters is: ",lettercount(str1))
    print("Count of letters is: ",lettercount(str2))
    print("Count of letters is: ",lettercount(str3))


if __name__=='__main__':
    main()
