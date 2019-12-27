'''
171. Excel Sheet Column Number
Easy
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''


def LeetCode171(word):

    num=1
    final_num=0
    for i in range(len(word)-1,-1,-1):
        key=ord(word[i])-ord('A')+1
        final_num=final_num+num*key
        num=26*num
    return final_num

def main():
    
    word='A'
    print(LeetCode171(word))

    word = 'AB'
    print(LeetCode171(word))

    word = 'ZY'
    print(LeetCode171(word))

if __name__=='__main__':
    main()