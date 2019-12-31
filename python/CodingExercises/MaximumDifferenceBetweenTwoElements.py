'''
Maximum difference between two elements such that larger element appears after the smaller number
Given an array arr[] of integers, find out the maximum difference between any two elements such that larger element appears after the smaller number.
Examples :

Input : arr = {2, 3, 10, 6, 4, 8, 1}
Output : 8
Explanation : The maximum difference is between 10 and 2.

Input : arr = {7, 9, 5, 6, 3, 2}
Output : 2
Explanation : The maximum difference is between 9 and 7.
'''

def MaximumDifferenceBetweenTwoElements(ary):

    max_diff=0
    minElement=ary[0]

    for i in range(1,len(ary)):

        if abs(ary[i]-minElement)>max_diff:
            max_diff=abs(ary[i]-minElement)

        if ary[i]<minElement:
            minElement=ary[i]
    return max_diff

def main():

    ary=[2, 3, 10, 6, 4, 8, 1]
    print(MaximumDifferenceBetweenTwoElements(ary))

    ary = [7, 9, 5, 6, 3, 2]
    print(MaximumDifferenceBetweenTwoElements(ary))


if __name__=='__main__':
    main()