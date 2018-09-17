'''
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
'''

import collections

def LeetCode58(str1):

    lst=str1.split()

    return len(lst[-1])

def main():
    
    str1='Hello World'
    print(LeetCode58(str1))

    str1 = 'Today is the   best day   '
    print(LeetCode58(str1))

    str1 = '  Show me     the   Money  '
    print(LeetCode58(str1))

if __name__=='__main__':
    main()