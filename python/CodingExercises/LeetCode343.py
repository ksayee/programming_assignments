'''
343. Integer Break
Medium
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

def GetProduct(tmp):

    product=1
    for i in range(0,len(tmp)):
        product=product*tmp[i]
    return product

def Combinations_recur(lst,tmp,fnl_lst,tgt):

    if tgt==0:
        product=GetProduct(tmp)
        if product in fnl_lst.keys():
            if sorted(tmp) not in fnl_lst[product]:
                fnl_lst[product].append(sorted(tmp.copy()))
        else:
            fnl_lst[product]=[]
            fnl_lst[product].append(sorted(tmp.copy()))
        return

    for i in range(0,len(lst)):
        if tgt<0:
            break
        tmp.append(lst[i])
        Combinations_recur(lst, tmp, fnl_lst, tgt-lst[i])
        tmp.pop()

def LeetCode343(num):

    lst=[]
    k=1
    while k<num:
        lst.append(k)
        k=k+1
    tmp=[]
    fnl_lst={}
    tgt=num
    Combinations_recur(lst,tmp,fnl_lst,tgt)
    return sorted(fnl_lst.items(),key=lambda x:x[0],reverse=True)[0]

def main():

    num=2
    print(LeetCode343(num))

    num = 10
    print(LeetCode343(num))

if __name__=='__main__':
    main()