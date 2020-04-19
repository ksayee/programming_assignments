'''
1417. Reformat The String
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.
Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.
Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
Example 4:
nput: s = "covid2019"
Output: "c2o0v1i9d"
Example 5:
Input: s = "ab123"
Output: "1a2b3"
'''

import collections

def Validate(tmp):

    for i in range(1,len(tmp)):
        key=tmp[i]
        if key>='a' and key<='z' and tmp[i-1]>='0' and tmp[i-1]<='9':
            pass
        elif key>='0' and key<='9' and tmp[i-1]>='a' and tmp[i-1]<='z':
            pass
        else:
            return False
    return True

def Combinations_recur(lst,cnt,tmp,fnl_lst,str1):

    if len(tmp)==len(str1):
        flg=Validate(tmp)
        if flg==True:
            if ''.join(tmp) not in fnl_lst:
                fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, str1)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1417(str1):

    char_cnt=0
    num_cnt=0
    for element in list(str1):
        if (element >='A' and element <='Z') or (element >='a' and element <='z'):
            char_cnt=char_cnt+1
        elif (element >='0' and element <='9'):
            num_cnt=num_cnt+1

    if abs(num_cnt-char_cnt)>1:
        return None

    dict=collections.Counter(str1)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,str1)
    return fnl_lst

def main():

    str1='a0b1c2'
    print(LeetCode1417(str1))

    str1 = 'leetcode'
    print(LeetCode1417(str1))

    str1 = '1229857369'
    print(LeetCode1417(str1))

    str1 = 'covid2019'
    print(LeetCode1417(str1))

    str1 = 'ab123'
    print(LeetCode1417(str1))

if __name__=='__main__':
    main()