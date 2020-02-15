# Given array nums = [-1, 2, 1, -4], and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

import collections

def Combinations_recur(lst,cnt,tmp,output_lst):

    if len(tmp)==3:
        val_sum=sum(tmp)
        if val_sum in output_lst.keys():
            if sorted(tmp) not in output_lst[val_sum]:
                output_lst[val_sum].append(sorted(tmp.copy()))
        else:
            output_lst[val_sum]=[]
            output_lst[val_sum].append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, output_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def TripleSumClosedTarget1(ary,target):
    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    output_lst={}
    Combinations_recur(lst,cnt,tmp,output_lst)

    min=999
    result=[]
    for key,val in output_lst.items():
        if abs(target-key)<min:
            min=abs(target-key)
            result=val
    return result

def TripleSumClosedTarget2(ary, target):

    ary.sort()
    min=999
    result=[]
    for i in range(0,len(ary)):
        left=i+1
        right=len(ary)-1
        while left<right:
            val_sum=ary[left]+ary[right]+ary[i]
            if abs(target-val_sum)<min:
                min=abs(target-val_sum)
                result=(ary[left],ary[right],ary[i])
                left=left+1
                right=right-1
            elif ary[left]+ary[right]+ary[i]<target:
                left=left+1
            else:
                right=right-1
    return result

def main():

    ary=[-1, 2, 1, -4]
    target=1
    print(TripleSumClosedTarget1(ary,target))
    print(TripleSumClosedTarget2(ary, target))

if __name__=='__main__':
    main()