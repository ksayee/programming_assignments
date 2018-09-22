'''
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
'''

import collections

def LeetCode290(ptrn, str1):

    p_dict=collections.Counter(ptrn)

    p_lst=[]
    for i in range(0,len(ptrn)):
        key=ptrn[i]
        p_lst.append(str(p_dict[key]))

    s_dict=collections.Counter(str1.split())

    s_lst=[]
    for key in str1.split():
        s_lst.append(str(s_dict[key]))

    if ''.join(p_lst)==''.join(s_lst):
        return True
    else:
        return False

def main():

    ptrn='abba'
    str1='dog cat cat dog'
    print(LeetCode290(ptrn,str1))

    ptrn = 'abba'
    str1 = 'dog cat cat fish'
    print(LeetCode290(ptrn, str1))

    ptrn = 'aaaa'
    str1 = 'dog cat cat dog'
    print(LeetCode290(ptrn, str1))

    ptrn = 'abba'
    str1 = 'dog dog dog dog'
    print(LeetCode290(ptrn, str1))

if __name__=='__main__':
    main()