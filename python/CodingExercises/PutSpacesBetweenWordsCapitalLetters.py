'''
Put spaces between words starting with capital letters
You are given an array of characters which is basically a sentence.
However there is no space between different words and the first letter of every word is in uppercase.
You need to print this sentence after following amendments:
(i) Put a single space between these words.
(ii) Convert the uppercase letters to lowercase.

Examples:

Input : BruceWayneIsBatman
Output : bruce wayne is batman

Input :  You
Output :  you
'''

def PutSpacesBetweenWordsCapitalLetters(str1):

    output_list=[]
    for i in range(0,len(str1)):
        key=str1[i]

        if key>='A' and key<='Z':
            if len(output_list)==0:
                output_list.append(key.lower())
            else:
                output_list.append(' ')
                output_list.append(key.lower())
        else:
            output_list.append(key)
    return ''.join(output_list)

def main():
    
    str1="BruceWayneIsBatman"
    print(PutSpacesBetweenWordsCapitalLetters(str1))

    str1 = "You"
    print(PutSpacesBetweenWordsCapitalLetters(str1))

if __name__=='__main__':
    main()