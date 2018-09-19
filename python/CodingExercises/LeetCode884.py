'''
884. Uncommon Words from Two Sentences

We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
'''

import collections
def LeetCode884(str1,str2):

    dict1=collections.Counter(str1.split())
    dict2=collections.Counter(str2.split())

    fnl_lst=[]
    for key,val in dict1.items():

        if val==1:
            if key not in dict2.keys():
                if key not in fnl_lst:
                    fnl_lst.append(key)

    for key,val in dict2.items():
        if val==1:
            if key not in dict1.keys():
                if key not in fnl_lst:
                    fnl_lst.append(key)

    return fnl_lst

def main():
    
    str1='this apple is sweet'
    str2='this apple is sour'
    print(LeetCode884(str1,str2))

    str1 = 'apple apple'
    str2 = 'banana'
    print(LeetCode884(str1, str2))

if __name__=='__main__':
    main()