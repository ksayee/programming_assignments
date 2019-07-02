'''
824. Goat Latin
Easy
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
The rules of Goat Latin are as follows:
If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.
Example 1:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:
Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
'''

def LeetCode824(str1):

    vow=['a','e','i','o','u']

    lst=str1.split(' ')

    fnl_lst=[]
    cnt=1
    for key in lst:

        if key[0].lower() in vow:
            fnl_str=key
        else:
            fnl_str=key[1:]+key[0]

        tmp=[]
        i=0
        while i<=cnt:
            tmp.append('a')
            i=i+1
        fnl_lst.append(fnl_str+'ma'+''.join(tmp))
        cnt=cnt+1

    return ' '.join(fnl_lst)

def main():

    str1='I speak Goat Latin'
    print(LeetCode824(str1))

    str1 = 'The quick brown fox jumped over the lazy dog'
    print(LeetCode824(str1))

if __name__=='__main__':
    main()