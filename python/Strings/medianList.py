def findMedian(ary):

    if len(ary)%2==0:

        indx1= int(len(ary)/2)-1
        indx2= int(len(ary)/2)

        tmp=(ary[indx1]+ary[indx2])/2

    else:
        tmp=ary[int(len(ary)/2)]

    return tmp

def main():
    ary1=[5,89,20,64,20,45]
    ary2 = [5, 89, 20, 64, 20, 45,45,23,67,32,30]
    ary1.sort()
    ary2.sort()

    print('Original List:', ary1)
    print('Maximum Element:', findMedian(ary1))

    print('Original List:', ary2)
    print('Maximum Element:', findMedian(ary2))

if __name__=='__main__':
    main()
