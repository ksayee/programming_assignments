'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you comp
'''

def DailyCodingProblem18(ary,k):

    i=0
    max=0
    dict={}
    while i<k:
        if ary[i]>max:
            max=ary[i]
        i=i+1

    dict[max]=ary[0:k]

    for j in range(1,len(ary)):
        st=j
        max=0
        if j+k<=len(ary):
            while j<st+k:
                if ary[j]>max:
                    max=ary[j]
                j=j+1
            if max in dict.keys():
                dict[max].append(ary[st:st+k])
            else:
                dict[max]=ary[st:st+k]

    return dict

def main():

    ary=[10, 5, 2, 7, 8, 7]
    k=3
    print(DailyCodingProblem18(ary,k))

if __name__=='__main__':
    main()