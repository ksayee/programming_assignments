'''
1190. Reverse Substrings Between Each Pair of Parentheses
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.
Example 1:
Input: s = "(abcd)"
Output: "dcba"
Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
Example 4:
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
'''


def LeetCode1190(str1):

    lst=[]
    for i in range(0,len(str1)):
        key=str1[i]
        if key==')':
            tmp=[]
            while lst[-1]!='(':
                tmp.append(lst[-1])
                lst.pop()
            lst.pop()
            for j in range(0,len(tmp)):
                lst.append(tmp[j])
        else:
            lst.append(key)
    return ''.join(lst)

def main():

    str1='(abcd)'
    print(LeetCode1190(str1))

    str1 = '(u(love)i)'
    print(LeetCode1190(str1))

    str1 = '(ed(et(oc))el)'
    print(LeetCode1190(str1))

    str1 = 'a(bcdefghijkl(mno)p)q'
    print(LeetCode1190(str1))

if __name__=='__main__':
    main()