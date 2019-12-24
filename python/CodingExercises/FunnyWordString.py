'''
Print all funny words in a string
We are given a sentence. Our task is to print all funny words/strings in that sentence.
What is a funny word ?
Reverse the given string. Iterate through each character of that string,
compare the absolute difference in the ASCII values of the characters at
positions 0 and 1, 1 and 2, 2 and 3 and so on to the end. If the list of
absolute differences is the same for both strings, they are funny otherwise not.
Examples:
Input  : HKMNPS
Output : Yes
Let r be the reverse of original string s
s = "HKMNPS"
r = "SPNMKH"
|H-K| = 3  = |S-P|
|K-M| = 2  = |P-N|
|M-N| = 1  = |N-M|
|N-P| = 2  = |M-K|
|P-S| = 3  = |K-H|
Since each comparison is equal so given string is funny

Input  : bdwy
Output : No
'''

def FunnyWordString(word):

    word_lst=list(word)
    rev_word_lst=list(reversed(word))

    for i in range(1,len(word_lst)):
        if abs(ord(word_lst[i-1])-ord(word_lst[i]))==abs(ord(rev_word_lst[i-1])-ord(rev_word_lst[i])):
            pass
        else:
            return False
    return True

def main():

    word='HKMNPS'
    print(FunnyWordString(word))

    word='bdwy'
    print(FunnyWordString(word))

    word = 'teaches '
    print(FunnyWordString(word))

    word = 'malayalam'
    print(FunnyWordString(word))

    word = 'arora'
    print(FunnyWordString(word))

if __name__=='__main__':
    main()