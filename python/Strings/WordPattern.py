# This is question from Cracking the coding interview. Chapter 1.9

def wordpattern(str1,pattern):

    lst={}
    st=0
    flg=1
    end=0
    j=0
    fnl_flg=1
    tmp=''
    for i in range(0,len(str1)):
        key=str1[i]

        while j<len(pattern):
            if pattern[j]==' ' or j+1==len(pattern):
                if j+1==len(pattern):
                    end=j+1
                else:
                    end=j
                tmp=pattern[st:end]
                flg=1
                j=j+1
                break
            else:
                if flg==1:
                    st=j
                    flg=0
                j=j+1


        if key in lst.keys():
            val=lst.get(key)
            if val==tmp:
                continue
            else:
                fnl_flg=0
                break
        else:
            lst[key]=tmp

    if fnl_flg==1:
        print('Strings are in Pattern')
    else:
        print('Strings are NOT in Pattern')


def main():

    str1='abba'
    pattern='dog cat cat dog'

    wordpattern(str1,pattern)

    str1 = 'abba'
    pattern = 'dog cat cat fish'

    wordpattern(str1, pattern)

    str1 = 'aaaa'
    pattern = 'dog cat cat dog'

    wordpattern(str1, pattern)

    str1 = 'abba'
    pattern = 'dog dog dog dog'

    wordpattern(str1, pattern)

if __name__=='__main__':
    main()
