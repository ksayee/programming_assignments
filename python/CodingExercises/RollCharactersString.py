'''
Roll the characters of string
Given a string s and an array roll where roll[i] represents rolling first roll[i] characters in string.
We need to apply every roll[i] on string and output final string. Rolling means increasing ASCII value of character, like rolling ‘z’ would result in ‘a’, rolling ‘b’ would result in ‘c’, etc.

constraints:
1 <= |s| <= 10^5
1 <= roll[i] <= 10^5

Examples:
Input : s = "bca"
        roll[] = {1, 2, 3}
Output : eeb

Explanation :
arr[0] = 1 means roll first character of string -> cca
arr[1] = 2 means roll first two characters of string -> dda
arr[2] = 3 means roll first three characters of string -> eeb
So final ans is "eeb"

Input : s = "zcza"
        roll[] = {1, 1, 3, 4}
Output : debb

'''

def RollCharactersString(word,roll):

    lst=list(word)
    for k in roll:
        tmp=lst[:k]
        for i in range(0,len(tmp)):
            letter=tmp[i]
            if letter=='z':
                tmp[i]='a'
            else:
                tmp[i]=chr(ord(letter)+1)
        tmp.extend(lst[k:])
        lst=tmp.copy()
    return ''.join(lst)

def main():

    word='bca'
    roll=[1, 2, 3]
    print(RollCharactersString(word,roll))

    word = 'zcza'
    roll = [1, 1, 3, 4 ]
    print(RollCharactersString(word, roll))
if __name__=='__main__':
    main()