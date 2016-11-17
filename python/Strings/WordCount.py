def wordcount(str1):

    count=0
    prev_char=' '
    for i in range(0,len(str1)):
        if (str1[i]==' ' and prev_char!=' ') or (i+1==len(str1) and prev_char!=' '):
            count=count+1
        prev_char=str1[i]
    return count

def main():
    str1 = 'I work in Amazon in Seattle'
    str2 = '    I    work    in    Amazon     in Seattle'
    str3 = 'I     work in    Amazon in     Seattle       '

    print('Count of words is ')
    print(wordcount(str1))
    print(wordcount(str2))
    print(wordcount(str3))

if __name__=='__main__':
    main()
