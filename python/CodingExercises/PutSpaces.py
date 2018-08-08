# Regex in Python to put spaces between words starting with capital letters
# Given an array of characters, which is basically a sentence. However, there is no space between different words and the first letter of every word is in uppercase. You need to print this sentence after following amendments:
# (i) Put a single space between these words.
# (ii) Convert the uppercase letters to lowercase.

def PutSpaces(str):

    fnl_lst=[]
    tmp_lst=[]

    flg=True

    for i in range(0,len(str)):
        key=str[i]

        if i==0:
            tmp_lst.append(key.lower())
        elif key>='A' and key <='Z':
            fnl_lst.append(''.join(tmp_lst))
            tmp_lst=[]
            tmp_lst.append(key.lower())
        else:
            tmp_lst.append(key)

    fnl_lst.append(''.join(tmp_lst))

    return ' '.join(fnl_lst)

def main():

    str='BruceWayneIsBatman'
    print(PutSpaces(str))

    str = 'GeeksForGeeks'
    print(PutSpaces(str))

if __name__=='__main__':
    main()