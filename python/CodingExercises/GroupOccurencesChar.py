# Group all occurrences of characters according to first appearance
# Given a string of lowercase characters, the task is to print the string in a manner such that a character comes first in string displays first with all its occurrences in string.

def GroupOccurences(str):

    ary=[0]*26

    for i in range(0,len(str)):
        key=str[i]
        k=ord(key)-97
        ary[k]=ary[k]+1
    fnl_lst=[]

    for i in range(0,len(str)):

        key=str[i]
        n=ord(key)-97
        k=0
        while k<ary[n]:
            fnl_lst.append(chr(n+97))
            k=k+1
        ary[n]=0
    return ''.join(fnl_lst)

def main():

    str='geeksforgeeks'
    print(GroupOccurences(str))

    str = 'occurrence'
    print(GroupOccurences(str))

    str = 'cdab'
    print(GroupOccurences(str))

if __name__=='__main__':
    main()