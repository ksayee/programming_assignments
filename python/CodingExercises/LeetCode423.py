'''
423. Reconstruct Original Digits from English
Medium
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.
Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"
Output: "012"
Example 2:
Input: "fviefuro"
Output: "45"
'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst,dict):

    if len(tmp)>0:
        if ''.join(tmp) in dict.keys():
            fnl_lst.append(str(dict[''.join(tmp)]))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, dict)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode423(dict,str1):

    str_dict=collections.Counter(str1)
    lst=[]
    cnt=[]
    for key,val in str_dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,dict)
    return ''.join(sorted(fnl_lst))

def main():

    dict={}
    dict['zero']=0
    dict['one'] = 1
    dict['two'] = 2
    dict['three'] = 3
    dict['four'] = 4
    dict['five'] = 5
    dict['six'] = 6
    dict['seven'] = 7
    dict['eight'] = 8
    dict['nine'] = 9

    str1='owoztneoer'
    print(LeetCode423(dict,str1))

    str1 = 'fviefuro'
    print(LeetCode423(dict,str1))

if __name__=='__main__':
    main()