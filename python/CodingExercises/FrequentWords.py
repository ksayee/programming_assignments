# Most frequent word in an array of strings
# Given an array of words find the most occurring word in it

import collections
def FrequentWords(ary):

    dict=collections.Counter(ary)

    sort=sorted(dict.items(),key=lambda x:x[1],reverse=True)

    return sort[0][0]

def main():

    ary=["geeks", "for", "geeks", "a",
                "portal", "to", "learn", "can",
                "be", "computer", "science",
                 "zoom", "yup", "fire", "in",
                 "be", "data"]
    print(FrequentWords(ary))

if __name__=='__main__':
    main()