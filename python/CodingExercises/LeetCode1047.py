'''
1047. Remove All Adjacent Duplicates In String
Easy
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
Example 1:
Input: "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
'''

def WordCompression(word):

    cnt=1
    prev=word[0]
    lst=[]
    for i in range(1,len(word)):
        curr=word[i]
        if prev!=curr:
            lst.append(prev)
            lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    lst.append(prev)
    lst.append(str(cnt))
    return ''.join(lst)

def WordExpansion(word):

    lst=[]
    for i in range(0,len(word)):
        key=word[i]
        try:
            cnt=int(key)
            k=0
            if cnt>1:
                pass
            else:
                while k<cnt:
                    lst.append(prev)
                    k=k+1

        except:
            prev=key
    return ''.join(lst)

def LeetCode1047(word):

    prev=''
    while True:
        compress=WordCompression(word)
        word=WordExpansion(compress)
        if len(word)==0:
            return 'NONE'
        if word==prev:
            break
        prev=word
    return word

def main():

    word='abbaca'
    print(LeetCode1047(word))

if __name__=='__main__':
    main()