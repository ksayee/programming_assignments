def uniquechar_hashmap(str1):

    lst={}
    for i in range(0,len(str1)):
        key=str1[i]
        if key in lst.keys():
            return False
        else:
            lst[key]=1
    return True

def uniquechar_list(str1):

    lst=[0]*256

    for i in range(0,len(str1)):
        key=str1[i]
        if lst[ord(key)]>0:
            return False
        else:
            lst[ord(key)]=1

    return True

def main():
    str1 = 'mary'

    print('Does this have unique character?', uniquechar_hashmap(str1))
    print('Does this have unique character?', uniquechar_list(str1))


if __name__=='__main__':
    main()
