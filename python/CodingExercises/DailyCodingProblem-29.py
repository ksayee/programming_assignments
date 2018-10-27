'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
'''

def DailyCodingProblem29(str1):

    lst=list(str1)
    fnl_lst=[]

    prev_chr=lst[0]
    cnt=1

    for i in range(1,len(lst)):

        curr_chr=lst[i]

        if prev_chr!=curr_chr:
            fnl_lst.append(str(cnt))
            fnl_lst.append(prev_chr)
            cnt=1
        else:
            cnt=cnt+1
        prev_chr=curr_chr
    fnl_lst.append(str(cnt))
    fnl_lst.append(prev_chr)

    return ''.join(fnl_lst)

def main():

    str1='AAAABBBCCDAA'
    print(DailyCodingProblem29(str1))

    str1 = 'AAAABBBCCDAAZ'
    print(DailyCodingProblem29(str1))

if __name__=='__main__':
    main()