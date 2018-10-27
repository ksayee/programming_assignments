'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2
'''

def GetMedian(tmp):

    if len(tmp)==1:
        return tmp[0]

    if len(tmp)%2!=0:
        mid=(len(tmp)//2)
        return tmp[mid]
    if len(tmp)%2==0:
        idx1=(len(tmp)//2)-1
        idx2=(len(tmp)//2)
        median=(tmp[idx1]+tmp[idx2])/2
        return median

def DailyCodingProblem33(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):

        tmp=ary[:i+1]
        tmp.sort()
        median=GetMedian(tmp)
        fnl_lst.append(median)
    return fnl_lst

def main():

    ary=[2, 1, 5, 7, 2, 0, 5]
    print(DailyCodingProblem33(ary))

if __name__=='__main__':
    main()