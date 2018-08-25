# Rearrange array such that even index elements are smaller and odd index elements are greater
# Given an array, rearrange the array such that :
# If index i is even, arr[i] <= arr[i+1]
# If index i is odd, arr[i] >= arr[i+1]

def RearrangeAryEvenOdd(ary):

    for i in range(0,len(ary)-1):

        if i%2==0:
            if ary[i]>ary[i+1]:
                tmp=ary[i+1]
                ary[i+1]=ary[i]
                ary[i]=tmp
        else:
            if ary[i]<ary[i+1]:
                tmp = ary[i + 1]
                ary[i + 1] = ary[i]
                ary[i] = tmp

    return ary

def main():

    ary=[2, 3, 4, 5]
    print(RearrangeAryEvenOdd(ary))

    ary = [6, 4, 2, 1, 8, 3]
    print(RearrangeAryEvenOdd(ary))

if __name__=='__main__':
    main()