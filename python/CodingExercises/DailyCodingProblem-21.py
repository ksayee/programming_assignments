'''
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def DailyCodingProblem21(ary):

    sort_lst=sorted(ary,key=lambda x:x[0])
    cnt=1

    tmp_lst=[]
    tmp_lst.append(sort_lst[0])
    k=0
    for i in range(1,len(sort_lst)):
        key=sort_lst[i]
        if key[0]>=tmp_lst[k][0] and key[0]<=tmp_lst[k][1]:
            cnt=cnt+1
        else:
            tmp_lst.append(key)
            k=k+1
    return cnt

def main():

    ary=[(30, 75), (0, 50), (60, 150)]
    print(DailyCodingProblem21(ary))

if __name__=='__main__':
    main()