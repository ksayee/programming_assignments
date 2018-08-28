# Move all Positive elements to end in order with extra space allowed
# Given an unsorted array of both negative and positive integer.
# The task is place all Positive element at the end of array without changing the order of positive element and negative element.

def MovePositiveNumbersEnd(ary):

    for i in range(1,len(ary)):

        key=ary[i]

        if key>0:
            continue

        k=i-1
        while (k>=0 and ary[k]>0):
            ary[k+1]=ary[k]
            k=k-1
        ary[k+1]=key

    return ary

def main():

    ary=[1, -1, 3, 2, -7, -5, 11, 6]
    print(MovePositiveNumbersEnd(ary))

    ary = [12,11,-13,-5,6,-7,5,-3,-6]
    print(MovePositiveNumbersEnd(ary))

    ary = [-5, 7, -3, -4, 9, 10, -1, 11]
    print(MovePositiveNumbersEnd(ary))

if __name__=='__main__':
    main()