# Extract maximum numeric value from a given string | Set 2 (Regex approach)
# Given an alphanumeric string, extract maximum numeric value from that string.

def MaxNumericaVal(str):

    lst=list(str)

    flg=False
    fnl_lst=[]
    tmp=[]

    for l in lst:

        if l>='0' and l<='9':
            tmp.append(l)
            flg=True
        else:
            if len(tmp)>0:
                fnl_lst.append(int(''.join(tmp)))
            tmp=[]
            flg=False

    if flg==True:
        fnl_lst.append(int(''.join(tmp)))

    max_val=sorted(fnl_lst,reverse=True)[0]

    return max_val

def main():
    
    str='100klh564abc365bg'
    print(MaxNumericaVal(str))

    str = 'abchsd0365sdhs'
    print(MaxNumericaVal(str))

    str = '100klh564abc365bg20uuu700'
    print(MaxNumericaVal(str))

if __name__=='__main__':
    main()