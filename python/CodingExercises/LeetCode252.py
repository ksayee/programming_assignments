'''
252. Meeting Rooms
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
'''

def LeetCode252(ary):

    lst=sorted(ary,key=lambda x:x[0])

    tmp=[]
    tmp.append(lst[0])
    cnt=1
    k=0
    for i in range(1,len(lst)):

        key=lst[i]

        if key[0]>tmp[k][0] and key[0]<tmp[k][1]:
            continue
        else:
            tmp.append(key)
            k=k+1
            cnt=cnt+1

    if cnt==len(ary):
        return True
    else:
        return False

def main():

    ary=[[0,30],[5,10],[15,20]]
    print(LeetCode252(ary))

    ary = [[7,10],[2,4]]
    print(LeetCode252(ary))

if __name__=='__main__':
    main()