'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def LeetCode14(ary):

    lst=sorted(ary,key=len )

    ptrn=list(lst[0])

    i=1
    while i <len(lst):

        if ''.join(ptrn) in lst[i][0:]:
            i=i+1
        else:
            i=1
            if len(ptrn)>0:
                ptrn.pop()
            else:
                break

    if len(ptrn)>0:
        return ''.join(ptrn)
    else:
        return -1

def main():
    
    ary=["flower","flow","flight"]
    print(LeetCode14(ary))

    ary = ["dog","racecar","car"]
    print(LeetCode14(ary))

if __name__=='__main__':
    main()