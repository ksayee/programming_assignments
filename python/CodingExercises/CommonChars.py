# Common characters in n strings
# Given n strings, find the common characters in all the strings. In simple words, find characters that appear in all the strings and display them in alphabetical order or lexicographical order.

def CommonChars(ary):

    fnl_lst=[]

    lst=[0]*26

    for l in ary:
        tmp=set(l)
        for k in tmp:
            n=ord(k)-97
            lst[n]=lst[n]+1

    for i in range(0,len(lst)):
        if lst[i]==len(ary):
            fnl_lst.append(chr(i+97))

    fnl_lst.sort()

    return fnl_lst

def main():

    ary=['geeksforgeeks', 'gemkstones', 'acknowledges', 'aguelikes']
    print(CommonChars(ary))

    ary = ['apple', 'orange']
    print(CommonChars(ary))

if __name__=='__main__':
    main()