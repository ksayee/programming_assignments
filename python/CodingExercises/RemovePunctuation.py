# Missing characters to make a string Pangram.

def RemovePunctuation(str1):

    fnl_lst=[]

    for i in range(0,len(str1)):

        if str1[i]==' ' or (str1[i]>='a' and str1[i]<='z') or (str1[i]>='A' and str1[i]<='Z'):
            fnl_lst.append(str1[i])
        else:
            continue

    return ''.join(fnl_lst)

def main():

    str1="%welcome' to @geeksforgeek<s"
    print(RemovePunctuation(str1))

    str1 = 'Hello!!!, he said ---and went.'
    print(RemovePunctuation(str1))

if __name__=='__main__':
    main()