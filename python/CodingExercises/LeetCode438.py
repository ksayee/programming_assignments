'''
438. Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

import collections

def LeetCode438(s,p):

    fnl_lst=[]
    for i in range(0,len(s)-len(p)+1):

        lst=list(s[i:i+len(p)])
        if ''.join(sorted(lst))==''.join(sorted(p)):
            fnl_lst.append(i)

    return fnl_lst


def main():

    s='cbaebabacd'
    p='abc'
    print(LeetCode438(s,p))

    s = 'abab'
    p = 'ab'
    print(LeetCode438(s, p))

if __name__=='__main__':
    main()