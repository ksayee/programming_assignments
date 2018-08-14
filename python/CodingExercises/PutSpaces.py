# Regex in Python to put spaces between words starting with capital letters
# Given an array of characters, which is basically a sentence. However, there is no space between different words and the first letter of every word is in uppercase. You need to print this sentence after following amendments:
# (i) Put a single space between these words.
# (ii) Convert the uppercase letters to lowercase.

def PutSpaces(str):

    lst=list(str)
    fnl_lst=[]
    tmp=[]
    for l in lst:
        if l>='A' and l<='Z':
            if len(tmp)>0:
                fnl_lst.append(''.join(tmp))
            tmp=[]
            tmp.append(l.lower())
        else:
            tmp.append(l)
    if len(tmp)>0:
        fnl_lst.append(''.join(tmp))

    return ' '.join(fnl_lst)

def main():

    str='BruceWayneIsBatman'
    print(PutSpaces(str))

    str = 'GeeksForGeeks'
    print(PutSpaces(str))

    str = 'You'
    print(PutSpaces(str))

if __name__=='__main__':
    main()