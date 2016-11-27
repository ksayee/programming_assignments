def reversevowels(str1):
    vow=[]
    vow.append('a')
    vow.append('e')
    vow.append('i')
    vow.append('o')
    vow.append('u')

    i=0
    j=len(str1)-1
    lst=['']*len(str1)

    while i<=j:
        if str1[i] not in vow:
            lst[i]=str1[i]
            i=i+1
            continue
        if str1[j] not in vow:
            lst[j] = str1[j]
            j=j-1
            continue

        lst[i]=str1[j]
        lst[j]=str1[i]
        i=i+1
        j=j-1

    return lst

def main():
    str1='hello'
    print('Reversing vowels',str1,reversevowels(str1))
    str2='leetcode'
    print('Reversing vowels', str2, reversevowels(str2))


if __name__=='__main__':
    main()
