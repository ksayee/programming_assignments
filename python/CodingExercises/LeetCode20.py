'''
https://leetcode.com/problems/valid-parentheses/description/
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

def LeetCode20(str1):

    lst=list(str1)

    fnl_lst=[]

    flg=True
    for i in range(0,len(lst)):

        key=lst[i]
        if key=='[' or key=='{' or key=='(':
            fnl_lst.append(key)
        else:
            if len(fnl_lst)==0:
                flg=False
                break
            else:
                if (key==')' and fnl_lst[-1]=='(') or (key==']' and fnl_lst[-1]=='[') or(key=='}' and fnl_lst[-1]=='{'):
                    fnl_lst.pop()
                else:
                    flg=False

    return flg

def main():

    str1='()'
    print(LeetCode20(str1))

    str1 = '()[]{}'
    print(LeetCode20(str1))

    str1 = '(]'
    print(LeetCode20(str1))

    str1 = '([)]'
    print(LeetCode20(str1))

    str1 = '{[]}'
    print(LeetCode20(str1))

if __name__=='__main__':
    main()