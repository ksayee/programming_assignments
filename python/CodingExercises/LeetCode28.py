'''
28. Implement strStr()

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

def LeetCode28(str1,str2):

    try:
        return str1.index(str2)
    except:
        return -1

def main():
    
    str1='hello'
    str2='ll'
    print(LeetCode28(str1,str2))

    str1 = 'aaaaa'
    str2 = 'bba'
    print(LeetCode28(str1,str2))

if __name__=='__main__':
    main()