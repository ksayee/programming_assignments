# Given two strings in lowercase, the task is to make them Anagram. The only allowed operation is to remove a character from any string. Find minimum number of characters to be deleted to make both the strings anagram?
# If two strings contains same data set in any order then strings are called Anagrams.

def toDict(str):

    dict={}
    lst=list(str)

    for l in lst:
        if l in dict.keys():
            dict[l]=dict.get(l)+1
        else:
            dict[l]=1
    return dict

def CharRemoveAnagram(s1,s2):

    if len(s1)>len(s2):
        big_lst=toDict(s1)
        sml_lst = toDict(s2)
    else:
        big_lst = toDict(s2)
        sml_lst = toDict(s1)

    cnt=0
    for key,val in big_lst.items():
        if key in sml_lst.keys():
            cnt=cnt+abs(val-sml_lst[key])
        else:
            cnt=cnt+val
    return cnt

def main():

    s1='bcadeh'
    s2='hea'
    print(CharRemoveAnagram(s1,s2))

    s1 = 'cddgk'
    s2 = 'gcd'
    print(CharRemoveAnagram(s1, s2))

    s1 = 'bca'
    s2 = 'acb'
    print(CharRemoveAnagram(s1, s2))

if __name__=='__main__':
    main()