'''
932. Beautiful Array
Medium
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
Given N, return any beautiful array A.  (It is guaranteed that one exists.)
Example 1:
Input: 4
Output: [2,1,4,3]
Example 2:
Input: 5
Output: [3,1,2,5,4]
'''

def Validate(tmp):

    flg=True
    for i in range(0,len(tmp)):
        for j in range(i+1,len(tmp)):
            diff=j-i
            if diff>1:
                val=(tmp[i]+tmp[j])//2
                idx=tmp.index(val)
                if idx>i and idx<j:
                    flg=False
                    break
    return flg

def Combinations_recur(lst,cnt,tmp,fnl_lst,num):

    if len(tmp)==num:
        flg=Validate(tmp)
        if flg==True:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,num)
        tmp.pop()
        cnt[i]=cnt[i]+1


def LeetCode932(num):

    i=1
    lst=[]
    cnt=[]
    while i<=num:
        lst.append(i)
        i=i+1
        cnt.append(1)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,num)
    return fnl_lst

def main():

    num=4
    print(LeetCode932(num))

    num = 5
    print(LeetCode932(num))

if __name__=='__main__':
    main()