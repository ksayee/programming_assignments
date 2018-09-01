# Minimum number of elements to add to make median equals x
# A median in an array with the length of n is an element which occupies position number (n+1)/2
# after we sort the elements in the non-decreasing order (the array elements are numbered starting with 1).
# A median of an array (2, 6, 1, 2, 3) is the number 2, and a median of array (0, 96, 17, 23) — the number 17.

def MedianMinElementAddedEqual(ary,k):

    l=0
    h=0
    e=0
    for i in range(0,len(ary)):

        if ary[i]==k:
            e=e+1
        if ary[i]<k:
            l=l+1
        if ary[i]>k:
            h=h+1

    cnt=0
    if l>h:
        cnt=l-h
    else:
        cnt=h-l-1

    return cnt+1-e

def main():

    ary=[10,20,30]
    k=10
    print(MedianMinElementAddedEqual(ary,k))

    ary = [1,2,3]
    k = 4
    print(MedianMinElementAddedEqual(ary,k))

if __name__=='__main__':
    main()