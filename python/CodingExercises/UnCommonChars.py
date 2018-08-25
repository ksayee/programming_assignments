# Find uncommon characters of the two strings
# Find and print the uncommon characters of the two given strings in sorted order. Here uncommon character means that either the character is present in one string or it is present in other string but not in both. The strings contain only lowercase characters and can contain duplicates.

def UnCommonChars(str1, str2):

    fnl_lst=[]

    lst1=set(str1)
    lst2=set(str2)

    for l in lst1:
        if l in lst2:
            continue
        else:
            fnl_lst.append(l)

    for l in lst2:
        if l in lst1:
            continue
        else:
            fnl_lst.append(l)

    fnl_lst.sort()

    return fnl_lst

def main():

    str1='characters'
    str2 = 'alphabets'
    print(UnCommonChars(str1,str2))

    str1 = 'geeksforgeeks'
    str2 = 'geeksquiz'
    print(UnCommonChars(str1, str2))

if __name__=='__main__':
    main()