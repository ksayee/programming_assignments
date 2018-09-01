# Count distinct elements in every window of size k
# Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k.

def DistinctElementsWindowSizeK(ary,k):

    fnl_lst=[]

    i=0
    j=k-1

    while j<len(ary):

        tmp=ary[i:j+1]
        tup=(tmp,len(set(tmp)))
        fnl_lst.append(tup)
        i=i+1
        j=j+1

    return fnl_lst


def main():

    ary=[1, 2, 1, 3, 4, 2, 3]
    k=4
    print(DistinctElementsWindowSizeK(ary,k))

if __name__=='__main__':
    main()