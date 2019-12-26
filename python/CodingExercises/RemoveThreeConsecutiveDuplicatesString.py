'''
Remove three consecutive duplicates from string
Given a string, you have to remove the three consecutive duplicates from the string. If no three are consecutive then output the string as it is.
Examples:
Input : aabbbaccddddc
Output :ccdc
Input :aabbaccddc
Output :aabbaccddc
'''

def Compression(word):

    lst=[]
    prev=word[0]
    curr=''
    cnt=1
    for i in range(1,len(word)):
        curr=word[i]
        if prev!=curr:
            if cnt<3:
                lst.append(prev)
                lst.append(str(cnt))
            elif cnt>=3:
                cnt=cnt-3
                if cnt>0:
                    lst.append(prev)
                    lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    if cnt!=3:
        lst.append(prev)
        lst.append(str(cnt))
    return ''.join(lst)

def Expansion(word):

    lst=[]
    prev=''
    curr=''
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

def RemoveThreeConsecutiveDuplicatesString(str1):

    curr=str1
    i=0
    while True:
        compressedWord=Compression(curr)
        expandedWord=Expansion(compressedWord)
        if curr==expandedWord:
            break
        curr=expandedWord
    return curr

def main():

    str1='aabbbaccddddc'
    print(RemoveThreeConsecutiveDuplicatesString(str1))

    str1 = 'aabbaccddc'
    print(RemoveThreeConsecutiveDuplicatesString(str1))

if __name__=='__main__':
    main()