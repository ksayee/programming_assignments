'''
253. Meeting Rooms II
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

def LeetCode252(ary):

    lst=sorted(ary,key=lambda x:x[0])

    room=1

    tmp=[]
    tmp.append(lst[0])
    k=0
    for i in range(1,len(lst)):

        key=lst[i]

        if key[0]>lst[k][0] and key[0]<lst[k][1]:
            room=room+1
        tmp.append(key)
        k=k+1
    return room


def main():

    ary=[[0,30],[5,10],[15,20]]
    print(LeetCode252(ary))

    ary = [[7,10],[2,4]]
    print(LeetCode252(ary))

if __name__=='__main__':
    main()