# Maximum consecutive repeating character in string
# Given a string, the task is to find maximum consecutive repeating character in string.

def MaxConsecRepeatingChar(str):

    curr_chr=str[0]
    prev_chr=str[0]
    max_cnt=0
    max_chr=''
    cnt=0

    for i in range(0,len(str)):

        curr_chr=str[i]
        if curr_chr!=prev_chr:
            if cnt>max_cnt:
                max_cnt=cnt
                max_chr=prev_chr
            cnt=1
        else:
            cnt=cnt+1
        prev_chr=curr_chr
    if cnt>max_cnt:
        max_cnt=cnt
        max_chr=prev_chr
    return max_chr

def main():

    str='geeekk'
    print(MaxConsecRepeatingChar(str))

    str = 'aaaabbcbbb'
    print(MaxConsecRepeatingChar(str))

if __name__=='__main__':
    main()