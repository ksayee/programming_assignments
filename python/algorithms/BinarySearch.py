def binarysearch(ary,key):

    low=0
    high=len(ary)-1

    while low<high:
        mid=int((low+high)/2)
        if key<ary[mid]:
            high=mid-1
        elif key>ary[mid]:
            low=mid+1
        else:
            return mid
    return -1

def main():

    ary = [5, 89, 20, 64, 19, 57,45,23,67,32,30]
    ary.sort()
    print(ary)
    key=67

    if binarysearch(ary,key)==-1:
        print('Element NOT found')
    else:
        print('Element Found at indx:', binarysearch(ary,key) )

if __name__=='__main__':
    main()
