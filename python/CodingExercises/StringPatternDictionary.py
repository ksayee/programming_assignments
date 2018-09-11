# Find all strings that match specific pattern in a dictionary
# Given a dictionary of words,
# find all strings that matches the given pattern where every character in the pattern is uniquely mapped to a character in the dictionary.

def GetHashValue(str1):

    dict={}
    fnl_lst=[]
    cnt=0
    for i in range(0,len(str1)):
        key=str1[i]
        if key in dict.keys():
            fnl_lst.append(str(dict[key]))
        else:
            cnt=cnt+1
            dict[key]=cnt
            fnl_lst.append(str(dict[key]))

    return ''.join(fnl_lst)

def StringPatternDictionary(lst, ptrn):

    hash_ptrn=GetHashValue(ptrn)

    fnl_lst=[]
    for key in lst:
        hash_val=GetHashValue(key)

        if hash_ptrn==hash_val:
            fnl_lst.append(key)

    return fnl_lst

def main():

    lst=["abb", "abc", "xyz", "xyy"]
    ptrn='foo'
    print(StringPatternDictionary(lst,ptrn))

    lst = ["abb", "abc", "xyz", "xyy"]
    ptrn = 'mno'
    print(StringPatternDictionary(lst, ptrn))

    lst = ["abb", "abc", "xyz", "xyy"]
    ptrn = 'aba'
    print(StringPatternDictionary(lst, ptrn))

    lst = ["abab", "aba", "xyz", "xyx"]
    ptrn = 'aba'
    print(StringPatternDictionary(lst, ptrn))

if __name__=='__main__':
    main()