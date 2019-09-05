'''
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true
'''

def LeetCode205(s,t):

    if len(s)!=len(t):
        return False

    dict={}

    for i in range(0,len(s)):
        key=s[i]

        if key in dict.keys():
            val=dict[key]
            if val!=t[i]:
                return False
        else:
            dict[key]=t[i]

    return True

def main():

    s = "egg"
    t = "add"
    print(LeetCode205(s,t))

    s = "foo"
    t = "bar"
    print(LeetCode205(s,t))

    s = "paper"
    t = "title"
    print(LeetCode205(s,t))

    s = "aab"
    t = "xxy"
    print(LeetCode205(s, t))

    s = "aab"
    t = "xyz"
    print(LeetCode205(s, t))

if __name__=='__main__':
    main()