'''
K’th Non-repeating Character
Given a string and a number k, find the k’th non-repeating character in the string.
Consider a large input string with lacs of characters and a small character set.
How to find the character by only doing only one traversal of input string?
Examples:
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.
Input : str = geeksforgeeks, k = 2
Output : o
Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.
'''

import collections
def PrintCharactersFrequencyOrderOfOccuernce(str1):

    dict=collections.Counter(str1)

    fnl_lst=[]
    for i in range(0,len(str1)):
        key=str1[i]
        if key in dict.keys():
            fnl_lst.append(key)
            fnl_lst.append(str(dict[key]))
            del dict[key]
    return ''.join(fnl_lst)

def main():
    
    str1='geeksforgeeks'
    print(PrintCharactersFrequencyOrderOfOccuernce(str1))

    str1 = 'elephant'
    print(PrintCharactersFrequencyOrderOfOccuernce(str1))

if __name__=='__main__':
    main()