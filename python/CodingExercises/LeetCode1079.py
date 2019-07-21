'''
1079. Letter Tile Possibilities
Medium
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.
Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:
Input: "AAABBC"
Output: 188
'''
import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)>0:
        if ''.join(tmp) not in fnl_lst:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode1079(str1):

    dict=collections.Counter(str1)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst)
    return len(fnl_lst)

def main():

    str1="AAB"
    print(LeetCode1079(str1))

    str1 = "AAABBC"
    print(LeetCode1079(str1))

if __name__=='__main__':
    main()