# Given an input string, expand the string.

def StringExpansion(str1):

    prev_chr=''
    curr_chr=''
    fnl_lst=[]
    for i in range(0,len(str1)):

        curr_chr=str1[i]

        if curr_chr>='1' and curr_chr<='9':
            n=int(curr_chr)
            k=0
            tmp=[]
            while k<n:
                tmp.append(prev_chr)
                k=k+1

            fnl_lst.append(''.join(tmp))
        prev_chr=curr_chr

    return ''.join(fnl_lst)

def main():

    str1='w4a3d1e1x6'
    print(StringExpansion(str1))

    str1 = 'a1'
    print(StringExpansion(str1))

    str1 = 'a1b2c4'
    print(StringExpansion(str1))

    str1 = 'a2b2c2d1'
    print(StringExpansion(str1))


if __name__=='__main__':
    main()