# k-th distinct (or non-repeating) element in an array.
# Given an integer array, print k-th distinct element in an array.
# The given array may contain duplicates and the output should print k-th element among all unique elements.
# If k is more than number of distinct elements, print -1.

def KthDistinctElement(ary,k):

    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]

        if key not in ary[i+1:] and key not in ary[:i]:
            fnl_lst.append(key)

    if k>len(fnl_lst):
        return -1
    else:
        return fnl_lst[k-1]
    
def main():
    
    ary=[1, 2, 1, 3, 4, 2]
    k=2
    print(KthDistinctElement(ary,k))

    ary = [1, 2, 50, 10, 20, 2]
    k = 3
    print(KthDistinctElement(ary,k))

    ary = [2, 2, 2, 2]
    k = 2
    print(KthDistinctElement(ary,k))

if __name__=='__main__':
    main()