'''
Merge two strings in chunks of given size
Given two strings ‘a’ and ‘b’ and a number k, our aim is to merge the
strings into a string s such that it contains groups of k characters from the strings alternately in the final string.

Examples:

Input: a = "durability",
      b = "essence
      k = 3
Output: duressabienclitey

Input: a = "determination"
      b = "stance"
      k = 3
Output: detstaermnceination
'''

def MergeTwoStringsGivenSize(str1,str2,k):

    lst=[]
    while True:
        if len(str1)==0:
            pass
        elif k<len(str1):
            lst.append(str1[:k])
            str1=str1[k:]
        else:
            lst.append(str1)
            str1=''

        if len(str2)==0:
            pass
        elif k<len(str2):
            lst.append(str2[:k])
            str2=str2[k:]
        else:
            lst.append(str2)
            str2=''
        if len(str1)==0 and len(str2)==0:
            break

    return ''.join(lst)

def main():

    str1='durability'
    str2='essence'
    k=3
    print(MergeTwoStringsGivenSize(str1,str2,k))

    str1 = 'determination'
    str2 = 'stance'
    k=3
    print(MergeTwoStringsGivenSize(str1, str2,k))

if __name__=='__main__':
    main()