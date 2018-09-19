'''
186. Reverse Words in a String II

Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
'''

def reverse(ary,left,right):

    while left<right:
        tmp=ary[left]
        ary[left]=ary[right]
        ary[right]=tmp
        left=left+1
        right=right-1

def LeetCode186(ary):

    left=0

    for i in range(0,len(ary)):

        if i==len(ary)-1:
            reverse(ary, left, i)
        elif ary[i]==' ':
            reverse(ary,left,i-1)
            left=i+1
    reverse(ary,0,len(ary)-1)
    return ''.join(ary)

def main():

    ary=["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(LeetCode186(ary))


if __name__=='__main__':
    main()