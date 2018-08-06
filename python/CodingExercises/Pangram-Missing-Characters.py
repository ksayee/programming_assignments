# Missing characters to make a string Pangram.

def PangramMissingCharacters(str1):

    print("Sentence:",str1)
    a=[0]*26

    for i in range(0,len(str1)):
        if str1[i]!=' ':
            key=str1[i].lower()
            a[ord(key)-97]=1

    fnl_lst=[]
    for i in range(0,len(a)):
        if a[i]==0:
            fnl_lst.append(chr(97+i))

    return ''.join(fnl_lst)

def main():

    str1='welcome to geeksforgeeks'
    print(PangramMissingCharacters(str1))

    str1 = 'The quick brown fox jumps'
    print(PangramMissingCharacters(str1))


if __name__=='__main__':
    main()