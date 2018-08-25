# Generate two output strings depending upon occurrence of character in input string.
# Given an input string str[], generate two output strings. One of which consists of those character which occurs only once in input string and second which consists of multi-time occurring characters. Output strings must be sorted.

def TwoOutputStrings(str):

    lst=[0]*26

    for i in range(0,len(str)):
        key=str[i]

        n=ord(key)-97
        lst[n]=lst[n]+1

    one_lst=[]
    two_lst=[]

    for i in range(0,len(lst)):
        if lst[i]==0:
            continue
        elif lst[i]==1:
            one_lst.append(chr(i+97))
        else:
            two_lst.append(chr(i+97))

    print("String with Characters occuring once:",''.join(one_lst))
    print("String with Characters occuring multiple times:",''.join(two_lst))

def main():

    str='geeksforgeeks'
    TwoOutputStrings(str)

    str = 'geekspractice'
    TwoOutputStrings(str)

if __name__=='__main__':
    main()