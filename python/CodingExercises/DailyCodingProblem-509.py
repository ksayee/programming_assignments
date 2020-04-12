'''
This problem was asked by Quora.
Given a string, find the palindrome that can be made by inserting the
fewest number of characters as possible anywhere in the word. If there is more than
one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".
'''

def DailyCodingProblem509(str1):

    matrix=[['' for i in range(0,len(str1))] for j in range(0,len(str1))]

    for i in range(0,len(str1)):
        matrix[i][i]=str1[i]

    for k in range(2,len(str1)+1):
        for i in range(0,len(str1)-k+1):
            j=i+k-1
            first=str1[i]
            last=str1[j]

            if str1[i]==str1[j]:
                matrix[i][j]=first+matrix[i+1][j-1]+last
            else:
                one=first+matrix[i+1][j]+first
                two = last + matrix[i][j-1] + last

                if len(one)<len(two):
                    matrix[i][j]=one
                elif len(two)<len(one):
                    matrix[i][j]=two
                else:
                    matrix[i][j]=min(one,two)

    for row in matrix:
        print(row)
    return matrix[0][-1]

def main():

    str1 = 'race'
    print(DailyCodingProblem509(str1))

    str1='google'
    print(DailyCodingProblem509(str1))

if __name__=='__main__':
    main()