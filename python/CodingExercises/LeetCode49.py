'''
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''

import collections

def LeetCode49(ary):

    dict={}

    for itm in ary:

        key=''.join(sorted(list(itm)))

        if key in dict.keys():
            dict[key].append(itm)
        else:
            tmp=[]
            tmp.append(itm)
            dict[key]=tmp

    fnl_lst=[]

    for key,val in dict.items():
        fnl_lst.append(val)

    return fnl_lst




def main():
    
    ary=["eat", "tea", "tan", "ate", "nat", "bat"]
    print(LeetCode49(ary))

if __name__=='__main__':
    main()