'''
Meta Strings (Check if two strings can become same after a swap in one string)
Given two strings, the task is to check whether these strings are meta strings or not.
Meta strings are the strings which can be made equal by exactly one swap in any of the strings.
Equal string are not considered here as Meta strings.
Examples:
Input : str1 = "geeks"
        str2 = "keegs"
Output : Yes
By just swapping 'k' and 'g' in any of string,
both will become same.

Input : str1 = "rsting"
        str2 = "string
Output : No

Input :  str1 = "Converse"
         str2 = "Conserve"
'''

def MetaStrings(str1,str2):

    if len(str1)!=len(str2):
        return False

    count=0
    lst=[]
    for i in range(0,len(str1)):
        key1=str1[i]
        key2=str2[i]
        if key1!=key2:
            count=count+1
            if count>2:
                return False
            tup=(key1,key2)
            lst.append(tup)

    if sorted(lst[0])==sorted(lst[1]):
        return True
    else:
        return False

def main():

    str1='geeks'
    str2='keegs'
    print(MetaStrings(str1,str2))

    str1 = 'rsting'
    str2 = 'string'
    print(MetaStrings(str1, str2))

    str1 = 'Converse'
    str2 = 'Conserve'
    print(MetaStrings(str1, str2))

if __name__=='__main__':
    main()