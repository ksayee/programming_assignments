# Count Strictly Increasing Subarrays
# Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing.
# Expected Time Complexity : O(n)
# Expected Extra Space: O(1)

def CountIncreasingSubArray(ary):

    cnt=0
    ln=1

    for i in range(0,len(ary)-1):

        if ary[i+1]>ary[i]:
            ln=ln+1
        else:
            cnt=cnt+int(((ln-1)*ln)/2)
            ln=1

    if ln>1:
        cnt = cnt + int(((ln - 1) * ln) / 2)
    return cnt

def main():

    ary=[1, 4, 3]
    print(CountIncreasingSubArray(ary))

    ary = [1, 2, 3, 4]
    print(CountIncreasingSubArray(ary))

    ary = [1, 2, 2, 4]
    print(CountIncreasingSubArray(ary))

    ary = [10, 20, 30, 40,50,60]
    print(CountIncreasingSubArray(ary))

if __name__=='__main__':
    main()