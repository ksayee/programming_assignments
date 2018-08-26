# Lexicographically next string
# Given a string, find lexicographically next string.

def LexicoNextString(str):

    lst=list(str)

    flg=False
    for i in range(len(lst)-1,-1,-1):
        key=lst[i]

        if key=='z':
            continue
        else:
            nxt_str=chr(ord(key)+1)
            lst[i]=nxt_str
            flg=True
            break

    if flg==True:
        return ''.join(lst)
    else:
        return ''.join(lst)+'a'

def main():
    
    str='geeks'
    print(LexicoNextString(str))

    str = 'raavz'
    print(LexicoNextString(str))

    str = 'zzz'
    print(LexicoNextString(str))

if __name__=='__main__':
    main()