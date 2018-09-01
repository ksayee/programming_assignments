# Implement Binary Search to find a Number

def BinarySearch(ary,k):

    l=0
    h=len(ary)-1

    while l<h:

        mid=int((l+h)/2)
        if ary[mid]==k:
            return "Found"
        else:
            if ary[mid]<k:
                l=mid+1
            else:
                h=mid-1

    return "Not Found"


def main():

    ary=[2, 3, 4, 10, 40]
    k=10
    print(BinarySearch(ary,k))

    ary = [2, 3, 4, 10, 40]
    k = 9
    print(BinarySearch(ary,k))


if __name__=='__main__':
    main()