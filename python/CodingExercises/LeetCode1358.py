'''
1358. Number of Substrings Containing All Three Characters
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.
Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:
Input: s = "abc"
Output: 1
'''

import collections

def LeetCode1358(str1,lst):

    input_lst=list(str1)
    cnt=0
    lgt=len(input_lst)
    dict={}
    flg=True
    k=0
    while k<len(input_lst):
        dict = {}
        for key in lst:
            try:
                idx=input_lst[k:].index(key)+k
                dict[key]=idx
            except:
                flg=False
                break
        if flg==False:
            break
        cnt = cnt + lgt - sorted(dict.items(), key=lambda x: x[1], reverse=True)[0][1]
        k=k+1
    return cnt

def main():

    str1='abcabc'
    lst=['a','b','c']
    print(LeetCode1358(str1,lst))

    str1 = 'aaacb'
    lst = ['a', 'b', 'c']
    print(LeetCode1358(str1, lst))

    str1 = 'abc'
    lst = ['a', 'b', 'c']
    print(LeetCode1358(str1, lst))


if __name__=='__main__':
    main()