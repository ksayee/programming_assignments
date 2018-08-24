# Reverse an array without affecting special characters
# Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.

def ReverseArraryWithoutSpecialChar(str1):

    lst=list(str1)
    tmp=[]
    for l in lst:
        if (l>='a' and l<='z') or (l>='A' and l<='Z'):
            tmp.append(l)
    tmp.reverse()

    fnl_lst=[]
    j=0
    for i in range(0,len(str1)):

        key=str1[i]

        if (key >= 'a' and  key<= 'z') or (key >= 'A' and key <= 'Z'):
            fnl_lst.append(tmp[j])
            j=j+1
        else:
            fnl_lst.append(key)

    return ''.join(fnl_lst)

def main():

    str1='a,b$c'
    print(ReverseArraryWithoutSpecialChar(str1))

    str1 = 'Ab,c,de!$'
    print(ReverseArraryWithoutSpecialChar(str1))

if __name__=='__main__':
    main()