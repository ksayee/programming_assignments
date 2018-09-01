# Check for Palindrome after every character replacement Query
# Given a string str and Q queries. Each query contains a pair of integers (i1, i2) and a character ‘ch’.
# We need to replace characters at indexes i1 and i2 with new character ‘ch’ and then tell if string str is palindrome or not.
# (0 <= i1, i2 < string_length) Examples:
'''
Input : str = “geeks”  Q = 2
        query 1: i1 = 3 ,i2 = 0, ch = ‘e’
        query 2: i1 = 0 ,i2 = 2 , ch = ‘s’
Output : query 1: “NO”
         query 2: “YES”
Explanation :
        In query 1 : i1 = 3 , i2 = 0 ch = ‘e’
                    After replacing char at index i1, i2
                    str[3] = ‘e’, str[0] = ‘e’
                    string become “eeees” which is not
                    palindrome so output “NO”
        In query 2 : i1 = 0 i2 = 2  ch = ‘s’
                    After replacing char at index i1 , i2
                     str[0] = ‘s’, str[2] = ‘s’
                    string become “seses” which is
                    palindrome so output “YES”

Input : str = “jasonamat”  Q = 3
        query 1: i1 = 3, i2 = 8 ch = ‘j’
        query 2: i1 = 2, i2 = 6 ch = ‘n’
        query 3: i1 = 3, i2 = 7 ch = ‘a’
Output :
       query 1: “NO”
       query 2: “NO”
       query 3: “YES”
'''

def Palindrome(lst):

    i=0
    j=len(lst)-1

    while i<j:
        if lst[i]!=lst[j]:
            return False
        i=i+1
        j=j-1

    return True

def CheckPalindromeCharReplacement(lst,i1,i2,ch):

    lst[i1]=ch
    lst[i2]=ch

    mid=int(len(lst)/2)+1
    print(Palindrome(lst))
    return lst

def main():

    str1='geeks'
    lst=list(str1)
    i1=3
    i2=0
    ch='e'
    lst=CheckPalindromeCharReplacement(lst,i1,i2,ch)
    i1 = 0
    i2 = 2
    ch = 's'
    lst=CheckPalindromeCharReplacement(lst, i1, i2, ch)

    str1 = 'jasonamat'
    lst = list(str1)
    i1 = 3
    i2 = 8
    ch = 'j'
    lst = CheckPalindromeCharReplacement(lst, i1, i2, ch)

    i1 = 2
    i2 = 6
    ch = 'n'
    lst = CheckPalindromeCharReplacement(lst, i1, i2, ch)

    i1 = 3
    i2 = 7
    ch = 'a'
    lst = CheckPalindromeCharReplacement(lst, i1, i2, ch)

if __name__=='__main__':
    main()