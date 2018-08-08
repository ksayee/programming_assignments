# Run Length Encoding in Python
# Given an input string, write a function that returns the Run Length Encoded string for the input string.

def StringCompression(str1):

    fnl_lst=[]

    chr=str1[0]
    prev_chr=chr
    cnt=1

    if len(str1)!=1:
        for i in range(1,len(str1)):
            chr=str1[i]

            if prev_chr!=chr:

                fnl_lst.append(prev_chr)
                fnl_lst.append(str(cnt))
                cnt=1
            else:
                cnt=cnt+1
            prev_chr=chr
    fnl_lst.append(prev_chr)
    fnl_lst.append(str(cnt))

    return ''.join(fnl_lst)

def main():

    str1='wwwwaaadexxxxxx'
    print(StringCompression(str1))

    str1 = 'a'
    print(StringCompression(str1))

    str1 = 'abbcccc'
    print(StringCompression(str1))

    str1 = 'aabbccd'
    print(StringCompression(str1))


if __name__=='__main__':
    main()