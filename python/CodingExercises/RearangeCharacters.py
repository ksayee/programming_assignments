# Rearrange characters in a string such that no two adjacent are same
# Given a string with repeated characters, task is rearrange characters in a string so that no two adjacent characters are same.

def RearangeCharacters(str1):

    fnl_lst=[]
    tmp_lst=[]
    k=-1
    j=-1
    for i in range(0,len(str1)):
        key=str1[i]
        if i==0:
            fnl_lst.append(key)
        else:
            if fnl_lst[j]==key:
                tmp_lst.append(key)
                k=k+1
            else:
                fnl_lst.append(key)
                j=j+1
                if len(tmp_lst) > 0:
                    item=tmp_lst[k]
                    fnl_lst.append(item)
                    k=k-1
                    tmp_lst.pop()
    if len(tmp_lst)>0:
        return "Not Possible"

    return ''.join(fnl_lst)

def main():

    str1="aaabc"
    print(RearangeCharacters(str1))

    str1 = "aaabb"
    print(RearangeCharacters(str1))

    str1 = "aa"
    print(RearangeCharacters(str1))

    str1 = "aaaabc"
    print(RearangeCharacters(str1))

if __name__=='__main__':
    main()