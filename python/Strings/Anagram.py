def anagram(str1,str2):
    lst={}

    if len(str1)!=len(str2):
        return False
    for i in range(0,len(str1)):
        if str1[i] in lst.keys():
            lst[str1[i]]=lst.get(str1[i])+1
        else:
            lst[str1[i]]=1

    for i in range(0, len(str2)):
        if str2[i] in lst and lst.get(str2[i])>0:
            lst[str2[i]] = lst.get(str2[i]) - 1
        else:
            return False

    return True

def main():
    str1='MARY'
    str2='ARMY'

    if anagram(str1, str2)==True:
        print('Strings are Anagrams')
    else:
        print('Strings are NOT Anagrams')

if __name__=='__main__':
    main()
