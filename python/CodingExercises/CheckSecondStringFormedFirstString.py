'''
Check whether second string can be formed from characters of first string
Given two strings str1 and str2, check if str2 can be formed from str1
Example :

Input : str1 = geekforgeeks, str2 = geeks
Output : Yes
Here, string2 can be formed from string1.

Input : str1 = geekforgeeks, str2 = and
Output :  No
Here string2 cannot be formed from string1.

Input : str1 = geekforgeeks, str2 = geeeek
Output :  Yes
Here string2 can be formed from string1
as string1 contains 'e' comes 4 times in
string2 which is present in string1.
'''

import collections
def CheckSecondStringFormedFirstString(str1,str2):

    dict1=collections.Counter(str1)
    dict2=collections.Counter(str2)

    for key,val in dict2.items():

        if key in dict1.keys() and dict1[key]>0:
            dict1[key]=dict1.get(key)-1
        else:
            return False
    return True

def main():
    
    str1='geekforgeeks'
    str2='geeks'
    print(CheckSecondStringFormedFirstString(str1,str2))

    str1 = 'geekforgeeks'
    str2 = 'and'
    print(CheckSecondStringFormedFirstString(str1, str2))

    str1 = 'geekforgeeks'
    str2 = 'geeeek'
    print(CheckSecondStringFormedFirstString(str1, str2))

if __name__=='__main__':
    main()