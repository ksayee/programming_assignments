# Non-overlapping sum of two sets
# Given two arrays A[] and B[] of size n.
# It is given that both array individually contain distinct elements. We need to find sum of all elements that are not common.

def NonOverlappingSumTwoList(ary1,ary2):

    sum=0

    for key in ary1:
        if key not in ary2:
            sum=sum+key

    for key in ary2:
        if key not in ary1:
            sum=sum+key

    return sum

def main():
    
    ary1=[1, 5, 3, 8]
    ary2 = [5, 4, 6, 7]
    print(NonOverlappingSumTwoList(ary1,ary2))

    ary1 = [1, 5, 3, 8]
    ary2 = [5, 1, 8, 3]
    print(NonOverlappingSumTwoList(ary1, ary2))

if __name__=='__main__':
    main()