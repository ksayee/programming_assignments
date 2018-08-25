# Find top three repeated in array
# Given an array of size N with repeated numbers, You Have to Find the top three repeated numbers.
# Note : If Number comes same number of times then our output is one who comes first in array

import collections

def Top3RepeatedElements(ary):

    dict=collections.Counter(ary)

    sort=sorted(dict.items(),key=lambda x:x[1],reverse=True)

    return sort[:3]

def main():

    ary=[3, 4, 2, 3, 16, 3, 15, 16, 15, 15, 16, 2, 3]
    print(Top3RepeatedElements(ary))

    ary = [2, 4, 3, 2, 3, 4, 5, 5, 3, 2, 2, 5]
    print(Top3RepeatedElements(ary))

if __name__=='__main__':
    main()