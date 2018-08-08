# Second most repeated word in a sequence in Python
# Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence. (Considering no two words are the second most repeated, there will be always a single word).

import collections
def SecondRepeated(lst):

    dict=collections.Counter(lst)
    print(dict.most_common())
    sort=sorted(dict.most_common(),key=lambda x:x[1], reverse=True)
    return sort[1][0]

def SecondRepeatedHashMap(lst):

    dict={}
    for l in lst:
        if l in dict.keys():
            dict[l]=dict.get(l)+1
        else:
            dict[l]=1

    sort=sorted(dict.items(),key=lambda x:x[1], reverse=True)
    print(sort)
    return sort[1][0]

def main():

    lst=["aaa", "bbb", "ccc", "bbb","aaa", "aaa"]
    print(SecondRepeated(lst))
    print(SecondRepeatedHashMap(lst))

    lst = ["geeks", "for", "geeks", "for","geeks", "aaa"]
    print(SecondRepeated(lst))
    print(SecondRepeatedHashMap(lst))

if __name__=='__main__':
    main()