'''
Recursively remove all adjacent duplicates
Given a string, recursively remove adjacent duplicate characters from the string. The output string should not have any adjacent duplicates. See following examples.
Examples:

Input: azxxzy
Output: ay
First “azxxzy” is reduced to “azzy”.
The string “azzy” contains duplicates,
so it is further reduced to “ay”.





Input: geeksforgeeg
Output: gksfor
First “geeksforgeeg” is reduced to
“gksforgg”. The string “gksforgg”
contains duplicates, so it is further
reduced to “gksfor”.

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac
'''

def Compression(word):

    lst=[]
    prev=word[0]
    curr=''
    cnt=1
    for i in range(1,len(word)):
        curr=word[i]
        if prev!=curr:
            if cnt>1:
                pass
            else:
                lst.append(prev)
                lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    if cnt==1:
        lst.append(prev)
        lst.append(str(cnt))
    return ''.join(lst)

def Expansion(word):

    lst=[]
    for i in range(0,len(word)):
        curr=word[i]
        try:
            cnt=int(curr)
            k=0
            while k<cnt:
                lst.append(prev)
                k=k+1
        except:
            pass
        prev=curr
    return ''.join(lst)

def RemoveAdjacentCharacters(str1):

    word=str1
    while True:
        compressWord=Compression(word)
        if len(compressWord)==0:
            word=''
            break
        expandedWord=Expansion(compressWord)
        if word==expandedWord or len(word)==0:
            break
        word=expandedWord
    return word

def main():

    str1='geeksforgeeg'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'azxxxzy'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'caaabbbaac'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'gghhg'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'aaaacddddcappp'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'aaaaaaaaaa'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'qpaaaaadaaaaadprq'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'acaaabbbacdddd'
    print(RemoveAdjacentCharacters(str1))

    str1 = 'acbbcddc'
    print(RemoveAdjacentCharacters(str1))

if __name__=='__main__':
    main()