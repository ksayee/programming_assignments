'''
Queries for characters in a repeated string
Given a string X. Form a string S by repeating string X multiple times i.e appending string X multiple times with itself.
There are Q queries of form i and j. The task is to print “Yes” if the element at index i
is same as the element at index j in S else print “No” for each query.
Examples :
Input : X = "geeksforgeeks", Q = 3.
Query 1: 0 8
Query 2: 8 13
Query 3: 6 15
Output :
Yes
Yes
No
String S will be "geeksforgeeksgeeksforgeeks....".
For Query 1, index 0 and index 8 have same element i.e 'g'.
For Query 2, index 8 and index 13 have same element i.e 'g'.
For Query 3, index 6 = 'o' and index 15 = 'e' which are not same.
'''

import collections
def QueriesCharactersRepeatedString(str1,query):

    idx1=query[0]
    idx2=query[1]

    while idx1>=len(str1):
        idx1=idx1-len(str1)

    while idx2>=len(str1):
        idx2 = idx2 - len(str1)

    if str1[idx1]==str1[idx2]:
        return True
    else:
        return False

def main():
    
    str1='geeksforgeeks'
    query=[0,8]
    print(QueriesCharactersRepeatedString(str1,query))

    query = [8,13]
    print(QueriesCharactersRepeatedString(str1,query))

    query = [6,15]
    print(QueriesCharactersRepeatedString(str1,query))

if __name__=='__main__':
    main()