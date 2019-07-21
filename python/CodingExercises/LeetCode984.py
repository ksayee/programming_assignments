'''
984. String Without AAA or BBB
Medium
Given two integers A and B, return any string S such that:
S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
Example 1:
Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:
Input: A = 4, B = 1
Output: "aabaa"
'''
import collections
import math

def Validate(tmp):

    try:
        idx1=''.join(tmp).index('aaa')
    except:
        idx1=-1

    try:
        idx2 = ''.join(tmp).index('bbb')
    except:
        idx2 = -1

    if idx1==-1 and idx2==-1:
        return True
    else:
        return False

def Combinations_recur(lst,cnt,tmp,fnl_lst,lgt):

    if len(tmp)==lgt:
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
        Combinations_recur(lst, cnt, tmp, fnl_lst, lgt)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode984(A, B):

    dict={}
    dict['a']=A
    dict['b']=B

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,A+B)
    return fnl_lst

def main():

    A=1
    B=2
    print(LeetCode984(A,B))

    A = 4
    B = 1
    print(LeetCode984(A, B))

if __name__=='__main__':
    main()