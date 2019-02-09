'''
This problem was asked by Google.
Find the minimum number of coins required to make n cents.
You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
'''

import collections
def DailyCodingProblem138(ary,tgt):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,tgt)
    return sorted(fnl_lst,key=lambda x:len(x))[0]

def Combinations_recur(lst,cnt,tmp,fnl_lst,tgt):

    if tgt==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        if tgt<0:
            break

        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,tgt-lst[i])
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=[1,5,10,25]
    tgt=16
    print(DailyCodingProblem138(ary,tgt))

if __name__=='__main__':
    main()