# You are passed a sorted array,
# write code that finds the number of “0”s in the array.
# Please try to implement this as a log N solution.
# If short on time, write pseudo-code and explain your implementation.

def FindZerosSortedArray(ary):
    l=0
    r=len(ary)-1

    flg=False

    while flg==False:
        m=(l+r)//2
        if ary[m]==0:
            flg=True
            break
        else:
            if ary[m]>0:
                r=m
            else:
                l=m
    cnt=1
    l_idx=m-1
    r_idx=m+1
    while ary[r_idx]==0:
        cnt=cnt+1
        r_idx=r_idx+1
    while ary[l_idx] == 0:
        cnt = cnt + 1
        l_idx = l_idx - 1
    return cnt

def main():

    ary =[-2,-2,-2,-1,-1,-1,0,0,0,0,0,0,1,1,1,2,2,2,3,3,3,4,4,5,6,7,7,8]
    print(FindZerosSortedArray(ary))

if __name__=='__main__':
    main()