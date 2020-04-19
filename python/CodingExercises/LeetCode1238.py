'''
1238. Circular Permutation in Binary Representation
Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :
p[0] = start
p[i] and p[i+1] differ by only one bit in their binary representation.
p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
Example 1:
Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01).
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]
Example 2:
Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).
'''

def GetBinary(num):

    tmp=num
    binary=[]
    while tmp>0:
        rem=tmp%2
        binary.append(str(rem))
        tmp=tmp//2
    binary.reverse()
    return ''.join(binary)

def Validate(tmp,dict,last_num):

    for i in range(1,len(tmp)):
        prev=dict[tmp[i-1]]
        curr=dict[tmp[i]]
        k=0
        diff=0
        while k<len(curr):
            if prev[k]!=curr[k]:
                diff=diff+1
            k=k+1
        if diff!=1:
            return False

    prev=dict[tmp[0]]
    curr=dict[tmp[last_num]]
    k = 0
    diff = 0
    while k < len(curr):
        if prev[k] != curr[k]:
            diff = diff + 1
        k = k + 1
    if diff != 1:
        return False
    return True

def Combinations_recur(lst,cnt,tmp,fnl_lst,dict,start,last_num):

    if len(tmp)==len(lst):
        if tmp[0]==start:
            flg=Validate(tmp,dict,last_num)
            if flg==True:
                fnl_lst.append(tmp.copy())
        return
    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, dict,start,last_num)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1238(n, start):

    first_num=0
    last_num=pow(2,n)-1
    dict={}
    num=first_num
    while num<=last_num:
        if num==0:
            dict[num]='0'
        else:
            dict[num]=GetBinary(num)
        num=num+1

    max_len=len(sorted(dict.items(),key=lambda x:len(x[1]),reverse=True)[0][1])
    for key,val in dict.items():
        if len(val)<max_len:
            cnt=0
            binary=list(val)
            while cnt+len(val)<max_len:
                binary.insert(0,'0')
                cnt=cnt+1
            dict[key]=''.join(binary)

    lst=list(dict.keys())
    cnt=[1]*len(dict.keys())

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,dict,start,last_num)
    return fnl_lst

def main():

    n=2
    start=3
    print(LeetCode1238(n,start))

    n = 3
    start = 2
    print(LeetCode1238(n, start))

if __name__=='__main__':
    main()