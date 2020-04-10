'''
1359. Count All Valid Pickup and Delivery Options
Given n orders, each order consist in pickup and delivery services.
Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).
Since the answer may be too large, return it modulo 10^9 + 7.
Example 1:
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:
Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:
Input: n = 3
Output: 90
'''

def Validate(tmp):
    for i in range(len(tmp)-1,-1,-1):
        key=tmp[i]
        if key[0]=='D':
            idxD=i
            idxP=tmp.index('P'+key[1])
            if idxP<idxD:
                pass
            else:
                return False
    return True

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==len(lst):
        flg=Validate(tmp)
        if flg==True:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1359(n):

    lst=[]
    cnt=[]
    i=1
    while i<=n:
        lst.append('P'+str(i))
        lst.append('D' + str(i))
        cnt.append(1)
        cnt.append(1)
        i=i+1

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst)
    return fnl_lst

def main():

    n=1
    print(LeetCode1359(n))

    n = 2
    print(LeetCode1359(n))

if __name__=='__main__':
    main()