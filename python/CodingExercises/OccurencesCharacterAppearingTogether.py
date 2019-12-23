'''
Check if all occurrences of a character appear together
Given a string s and a character c, find if all occurrences of c appear together in s or not.
If the character c does not appear in the string at all, the answer is true.
Examples
Input: s = "1110000323", c = '1'
Output: Yes
All occurrences of '1' appear together in
"1110000323"
Input: s  = "3231131", c = '1'
Output: No
All occurrences of 1 are not together
Input: s  = "abcabc", c = 'c'
Output: No
All occurrences of 'c' are not together
Input: s  = "ababcc", c = 'c'
Output: Yes
All occurrences of 'c' are together
'''

def OccurencesCharacterAppearingTogether(str1,letter):

    found=False
    flag=False
    for i in range(0,len(str1)):
        key=str1[i]

        if key==letter:
            if found==False and flag==False:
                found=True
                flag=True
            elif found==True and flag==True:
                pass
            elif found==True and flag==False:
                return False
        else:
            flag=False

    if found==True:
        return True
    else:
        return False

def main():
    
    str1='1110000323'
    letter='1'
    print(OccurencesCharacterAppearingTogether(str1,letter))

    str1 = '3231131'
    letter = '1'
    print(OccurencesCharacterAppearingTogether(str1, letter))

    str1 = '3231131'
    letter = 'c'
    print(OccurencesCharacterAppearingTogether(str1, letter))

    str1 = 'ababcc'
    letter = 'c'
    print(OccurencesCharacterAppearingTogether(str1, letter))

if __name__=='__main__':
    main()