'''
1209. Remove All Adjacent Duplicates in String II
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them
causing the left and the right side of the deleted substring to concatenate together.
We repeatedly make k duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.
Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
'''

def GetCompression(candy,k):

    lst=[]
    cnt=1
    prev=candy[0]
    for i in range(1,len(candy)):
        curr=candy[i]
        if prev!=curr:
            if k<cnt:
                lst.append(prev)
                lst.append(str(cnt-k))
            elif k>cnt:
                lst.append(prev)
                lst.append(str(cnt))
            cnt=1
        else:
            cnt=cnt+1
        prev=curr
    if k < cnt:
        lst.append(prev)
        lst.append(str(cnt - k))
    elif k > cnt:
        lst.append(prev)
        lst.append(str(cnt))
    return ''.join(lst)

def GetExpansion(compress):
    lst=[]

    for i in range(0,len(compress)):
        key=compress[i]
        if key>='1' and key<='9':
            cnt=0
            while cnt<int(key):
                lst.append(prev)
                cnt=cnt+1
        prev=compress[i]
    return ''.join(lst)

def LeetCode1209(candy, k):

    prev=''
    while True:
        compress=GetCompression(candy,k)
        if len(compress)==0:
            return ''
        candy=GetExpansion(compress)
        if prev==candy:
            break
        prev=candy
    return candy

def main():

    str1='abcd'
    k=2
    print(LeetCode1209(str1,k))

    str1 = 'deeedbbcccbdaa'
    k = 3
    print(LeetCode1209(str1, k))

    str1 = 'pbbcggttciiippooaais'
    k = 2
    print(LeetCode1209(str1, k))

if __name__=='__main__':
    main()