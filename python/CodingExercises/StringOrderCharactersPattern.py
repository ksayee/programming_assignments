# Check if string follows order of characters defined by a pattern or not | Set 2
# Given an input string and a pattern,
# check if characters in the input string follows the same order as determined by characters present in the pattern.
# Assume there won’t be any duplicate characters in the pattern.

def RemoveDuplicateString(lst):

    fnl_lst=[]
    prev_chr=''
    for key in lst:
        if prev_chr!=key:
            fnl_lst.append(key)
        prev_chr=key
    print(''.join(fnl_lst))
    return ''.join(fnl_lst)

def StringOrderCharactersPattern(str1, ptrn):

    ptrn_lst=list(ptrn)
    lst=[]
    for i in range(0,len(str1)):
        key=str1[i]
        if key in ptrn_lst:
            lst.append(key)

    fnl_str=RemoveDuplicateString(lst)

    if ptrn==fnl_str:
        return True
    else:
        return False

def main():

    str1='engineers rock'
    ptrn='er'
    print(StringOrderCharactersPattern(str1,ptrn))

    str1 = 'engineers rock'
    ptrn = 'egr'
    print(StringOrderCharactersPattern(str1, ptrn))

    str1 = 'engineers rock'
    ptrn = 'gsr'
    print(StringOrderCharactersPattern(str1, ptrn))

    str1 = 'bfbaeadeacc'
    ptrn = 'bac'
    print(StringOrderCharactersPattern(str1, ptrn))

if __name__=='__main__':
    main()