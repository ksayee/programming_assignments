'''
942. DI String Match
Easy
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
Example 1:
Input: "IDID"
Output: [0,4,1,3,2]
Example 2:
Input: "III"
Output: [0,1,2,3]
Example 3:
Input: "DDI"
Output: [3,2,0,1]
'''

def Validate(tmp,str1):

    str_lst=list(str1)
    j=0
    flg=True
    for i in range(1,len(tmp)):

        if str_lst[j]=='I':
            if tmp[i]>tmp[i-1]:
                pass
            else:
                flg=False
                break
        elif str_lst[j]=='D':
            if tmp[i]<tmp[i-1]:
                pass
            else:
                flg=False
                break
        j=j+1
    return flg

def Combination_recur(lst,cnt,tmp,fnl_lst,str1):

    if len(tmp)==len(lst):
        flg=Validate(tmp,str1)
        if flg==True:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combination_recur(lst, cnt, tmp, fnl_lst,str1)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode942(str1):

    lst=[]
    cnt=[]
    i=0
    while i<=len(str1):
        lst.append(i)
        i=i+1
        cnt.append(1)

    tmp=[]
    fnl_lst=[]

    Combination_recur(lst,cnt,tmp,fnl_lst,str1)
    return fnl_lst[0]

def main():

    str1='IDID'
    print(LeetCode942(str1))

    str1 = 'III'
    print(LeetCode942(str1))

    str1 = 'DDI'
    print(LeetCode942(str1))

if __name__=='__main__':
    main()