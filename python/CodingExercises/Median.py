# Find median of an Array of numbers

def Median(ary):

    ary.sort()
    print(ary)

    if len(ary)%2!=0:
        mid=int(len(ary)/2)
        return ary[mid]
    else:
        idx1=int(len(ary)/2)-1
        idx2=int(len(ary)/2)

        return (ary[idx1]+ary[idx2])/2

def main():

    ary=[5, 89, 20, 64, 20, 45]
    print(Median(ary))

    ary = [5, 89, 20, 64, 20, 45, 45, 23, 67, 32, 30]
    print(Median(ary))

if __name__=='__main__':
    main()