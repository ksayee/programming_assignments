'''
32. Longest Valid Parentheses
Hard
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

import collections

def LeetCode32(str1):

    lst=list(str1)
    stk=[]
    pointers=[]

    for i in range(0,len(lst)):
        key=lst[i]
        if key=='(':
            stk.append(key)
            pointers.append(i)
        elif key==')':
            if len(stk)==0:
                stk.append(key)
                pointers.append(i)
            elif stk[-1]=='(':
                stk.pop()
                pointers.pop()
            else:
                stk.append(key)
                pointers.append(i)

    tmp=[]

    if len(pointers)==0:
        val=len(lst)-1
        tmp.append(val)
    elif len(pointers)==1:
        val=len(lst)-pointers[-1]-1
        if val>0:
            tmp.append(val)
    else:
        for i in range(1,len(pointers)):
            val=pointers[i]-pointers[i-1]-1
            if val>0:
                tmp.append(val)
        val=len(lst)-pointers[-1]-1
        if val>0:
            tmp.append(val)
    return tmp

def main():

    str1='(()'
    print(LeetCode32(str1))

    str1 = ')()())'
    print(LeetCode32(str1))

    str1 = '(()(((()(()))'
    print(LeetCode32(str1))

    str1 = ')))(())())))(()()()(())))))'
    print(LeetCode32(str1))

if __name__=='__main__':
    main()