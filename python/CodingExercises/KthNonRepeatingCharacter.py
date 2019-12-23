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

def KthNonRepeatingCharacter(str1,k):

    dict={}
    stk=[]
    for i in range(0,len(str1)):
        key=str1[i]

        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

        if dict[key]==1:
            stk.append(key)
        else:
            try:
                idx=stk.index(key)
                del stk[idx]
            except:
                pass
    if k-1<len(stk):
        return stk[k-1]
    else:
        return "Not Existing"

def main():
    
    str1='geeksforgeeks'
    k=3
    print(KthNonRepeatingCharacter(str1,k))

    str1 = 'geeksforgeeks'
    k = 2
    print(KthNonRepeatingCharacter(str1, k))

    str1 = 'geeksforgeeks'
    k = 4
    print(KthNonRepeatingCharacter(str1, k))

if __name__=='__main__':
    main()