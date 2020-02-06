'''
Given a sorted array, return the number of times an item appears in an array.
ary=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]
'''


def ReturnCountOfTimesItemAppearsSortedArrayUber1(ary,num):

    dict={}

    for key in ary:
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1
    if num in dict.keys():
        return dict[num]
    else:
        return -1

def ReturnCountOfTimesItemAppearsSortedArrayUber2(ary,num):

    cnt=0

    left=0
    right=len(ary)-1

    while left<right:
        mid=(left+right)//2

        if ary[mid]==num:
            cnt=cnt+1
            k=mid-1
            if mid-1<0:
                break
            while True:
                if ary[k]==num:
                    cnt=cnt+1
                    if k>0:
                        k=k-1
                    else:
                        break
                else:
                    break
            if mid+1==len(ary):
                break
            k=mid+1
            while True:
                if ary[k]==num:
                    cnt=cnt+1
                    if k<len(ary)-1:
                        k=k+1
                    else:
                        break
                else:
                    break
            break
        elif num<ary[mid]:
            right=mid-1
        elif num>ary[mid]:
            left=mid+1

    if cnt==0:
        return -1
    else:
        return cnt

def main():

    ary=[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]

    print(ReturnCountOfTimesItemAppearsSortedArrayUber1(ary,2))
    print(ReturnCountOfTimesItemAppearsSortedArrayUber2(ary, 2))

    print(ReturnCountOfTimesItemAppearsSortedArrayUber1(ary, 5))
    print(ReturnCountOfTimesItemAppearsSortedArrayUber2(ary, 5))

    print(ReturnCountOfTimesItemAppearsSortedArrayUber1(ary, 1))
    print(ReturnCountOfTimesItemAppearsSortedArrayUber2(ary, 1))

    print(ReturnCountOfTimesItemAppearsSortedArrayUber1(ary, 4))
    print(ReturnCountOfTimesItemAppearsSortedArrayUber2(ary, 4))

if __name__=='__main__':
    main()