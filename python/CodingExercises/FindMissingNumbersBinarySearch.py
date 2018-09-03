# Find the nth missing number efficiently.

def FindNthMissingNumberBinarySearch(ary,k):

    ary.sort()
    left=0
    right=len(ary)-1

    while left < right:
        mid= int((left+right)/2)
        miss_nums=(ary[mid]-ary[left]+1)-(mid-left+1)
        if mid-left==1:
            break
        if k<=miss_nums:
            right=mid
        else:
            left=mid
            k=k-miss_nums
    fnl_lst=[]

    tmp=ary[left]+1

    while tmp<ary[right]:
        if tmp not in ary:
            fnl_lst.append(tmp)
        tmp=tmp+1

    return fnl_lst[k-1]

def main():

    ary=[2, 5, 6, 3, 9]
    k=2
    print(FindNthMissingNumberBinarySearch(ary,k))

    ary = [1, 7, 3, 13, 5, 10, 8, 4, 9]
    k=3
    print(FindNthMissingNumberBinarySearch(ary,k))

    ary = [10, 13, 14, 15, 18, 22, 30, 31, 32,35]
    k=16
    print(FindNthMissingNumberBinarySearch(ary,k))

if __name__=='__main__':
    main()