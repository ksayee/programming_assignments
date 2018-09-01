# Minimum insertions to form a palindrome with permutations allowed
# Given a string of lowercase letters.
# Find minimum characters to be inserted in string so that it can become palindrome. We can change positions of characters in string.

def PalindromeMinimumInsertions(str1):

    lst=[0]*26

    for i in range(0,len(str1)):

        key=str1[i]

        lst[97-ord(key)]=lst[97-ord(key)]+1

    cnt=0
    for i in range(0,len(lst)):
        if lst[i]!=0:
            if lst[i]%2==1:
                cnt=cnt+1
    return cnt-1

def main():

    str1='geeksforgeeks'
    print(PalindromeMinimumInsertions(str1))

    str1 = 'aabbc'
    print(PalindromeMinimumInsertions(str1))

if __name__=='__main__':
    main()