'''
524. Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
'''

def Validate(word,wordList):

    if word in wordList:
        return True
    else:
        return False

def Combination_recur(lst,cnt,tmp,fnl_lst,wordList):

    if len(tmp)>0:
        flg=Validate(''.join(tmp),wordList)
        if flg==True:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combination_recur(lst, cnt, tmp, fnl_lst, wordList)
        cnt[i]=cnt[i]+1
        tmp.pop()

import collections
def LeetCode524(str1, wordList):

    dict=collections.Counter(str1)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]

    Combination_recur(lst,cnt,tmp,fnl_lst,wordList)
    return sorted(fnl_lst,key=lambda x:len(x),reverse=True)[0]

def main():

    str1='abpcplea'
    wordList=["ale","apple","monkey","plea"]
    print(LeetCode524(str1,wordList))

    str1 = 'abpcplea'
    wordList = ["a","b","c"]
    print(LeetCode524(str1, wordList))

if __name__=='__main__':
    main()