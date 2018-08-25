# Find a peak element
# Given an array of integers. Find a peak element in it. An array element is peak if it is NOT smaller than its neighbors.
# For corner elements, we need to consider only one neighbor.
# For example, for input array {5, 10, 20, 15}, 20 is the only peak element.
# For input array {10, 20, 15, 2, 23, 90, 67}, there are two peak elements: 20 and 90. Note that we need to return any one peak element.
# Following corner cases give better idea about the problem.
# 1) If input array is sorted in strictly increasing order, the last element is always a peak element. For example, 50 is peak element in {10, 20, 30, 40, 50}.
# 2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 100 is the peak element in {100, 80, 60, 50, 20}.
# 3) If all elements of input array are same, every element is a peak element.

def PeakElement(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):

        if i==0:
            if ary[i]>=ary[i+1]:
                fnl_lst.append(ary[i])
        elif i==len(ary)-1:
            if ary[i]>=ary[i-1]:
                fnl_lst.append((ary[i]))
        else:
            if ary[i]>=ary[i+1] and ary[i]>=ary[i-1]:
                fnl_lst.append(ary[i])

    return fnl_lst

def main():
    
    ary=[1, 3, 20, 4, 1, 0]
    print(PeakElement(ary))

    ary = [5, 10, 20, 15]
    print(PeakElement(ary))

    ary=[10, 20, 15, 2, 23, 90, 67]
    print(PeakElement(ary))

if __name__=='__main__':
    main()