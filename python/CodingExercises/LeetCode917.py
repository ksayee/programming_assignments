'''
917. Reverse Only Letters
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
Example 1:
Input: "ab-cd"
Output: "dc-ba"
Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''

def LeetCode917(str1):

    lst=list(str1)

    left=0
    right=len(lst)-1

    while left<right:

        if (lst[left]>='a' and lst[left]<='z') or (lst[left]>='A' and lst[left]<='Z'):
            l_flg=True
        else:
            l_flg=False
            left=left+1

        if (lst[right]>='a' and lst[right]<='z') or (lst[right]>='A' and lst[right]<='Z'):
            r_flg=True
        else:
            r_flg=False
            right=right-1

        if l_flg==True and r_flg==True:
            tmp=lst[left]
            lst[left]=lst[right]
            lst[right]=tmp
            left=left+1
            right=right-1

    return ''.join(lst)

def main():

    str1='ab-cd'
    print(LeetCode917(str1))

    str1 = 'a-bC-dEf-ghIj'
    print(LeetCode917(str1))

    str1 = 'Test1ng-Leet=code-Q!'
    print(LeetCode917(str1))

if __name__=='__main__':
    main()