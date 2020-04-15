'''
1. Password Creation A password manager wants to create new passwords using
two strings given by the user, then combined to create a harder-to-guess combination.
Given two strings, interleave the characters of the strings to create a new string.
Beginning with an empty string, alternately append a character from string a and from string b.
If one of the strings is exhausted before the other, append the remaining letters from the other string all at once.
The result is the new password. Example If a = "hackerrank' and b = mountain, the result is hmaocuknetrariannk.
Function Description Complete the function newPassword in the editor below. newPassword has the following parameter(s):
string a: the first string. string b: the second string Returns: string: the merged string Constraints • 1 s lengths of a, b s 25000 •
All characters in a and b are lowercase letters in the range ascii['a'-'2']
Input Format For Custom Testing Input from stdin will be processed as follows and passed to the function:
The first line contains the string a. The second line contains the string b. Sample Case o Sample
Input STDIN Function abc def → + a= 'abc b = 'def! Sample Output adbecf Explanation
Alternately taking characters from each string, the merged string is 'adbecf Sample Case 1
Sample Input STDIN Function cat - rabbit a 'cat! b = 'rabbit! Sample Output craatbbit
Explanation Alternately taking characters from each string, the merged string is "craatbbit.
After a is exhausted, the remainder of bis concatenated to get 'craatbbit.
'''

#hmaocuknetrariannk
#hmaocuknetrarian
#craatbbit
def PasswordCreationManager(str1,str2):

    tmp=[]
    m=0
    n=0
    flg=False
    while m!=-1 or n!=-1:
        if flg==False:
            if m==-1:
                pass
            else:
                if m==len(str1)-1:
                    tmp.append(str1[m])
                    m=-1
                else:
                    tmp.append(str1[m])
                    m=m+1
            flg=True
        elif flg==True:
            if n==-1:
                pass
            else:
                if n==len(str2)-1:
                    tmp.append(str2[n])
                    n=-1
                else:
                    tmp.append(str2[n])
                    n=n+1
            flg=False
        if m==-1 and n==-1:
            break
    return ''.join(tmp)

def main():
    
    str1='hackerrank'
    str2='mountain'
    print(PasswordCreationManager(str1,str2))

    str1 = 'cat'
    str2 = 'rabbit'
    print(PasswordCreationManager(str1, str2))

if __name__=='__main__':
    main()