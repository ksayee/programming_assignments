'''
57. Insert Interval
Hard
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

def LeetCode57(intervals,newInterval):

    sortIntervals=sorted(intervals,key=lambda x:x[0])

    output_lst=[]
    output_lst.append(sortIntervals[0])
    k=0
    addFlag=False
    for i in range(1,len(sortIntervals)):
        key=sortIntervals[i]
        if addFlag==False:
            if newInterval[0]<output_lst[k][1] and newInterval[1]<output_lst[k][1]:
                addFlag=True
                pass
            elif newInterval[0]>output_lst[k][1] and newInterval[1]<key[0]:
                tmp=[]
                tmp.append(newInterval[0])
                tmp.append(newInterval[1])
                output_lst.append(tmp.copy())
                k=k+1
                addFlag=True
            elif newInterval[0]>output_lst[k][1] and key[0]<newInterval[0]:
                tmp=[]
                tmp.append(key[0])
                if newInterval[1]<key[1]:
                    tmp.append(key[1])
                elif key[1]<newInterval[1]:
                    tmp.append(newInterval[1])
                output_lst.append(tmp.copy())
                k=k+1
                addFlag=True
            elif newInterval[0]<output_lst[k][1] and newInterval[1]<key[0]:
                tmp=[]
                tmp.append(output_lst[k][0])
                tmp.append(newInterval[1])
                del output_lst[k]
                output_lst.append(tmp.copy())
                output_lst.append(key.copy())
                k=k+1
                addFlag=True
        else:
            if key[0]<output_lst[k][1] and key[1]<output_lst[k][1]:
                pass
            elif key[0]<=output_lst[k][1] and key[1]>output_lst[k][1]:
                tmp=[]
                tmp.append(output_lst[k][0])
                tmp.append(key[1])
                del output_lst[k]
                output_lst.append(tmp.copy())
            elif key[0]>output_lst[k][1]:
                tmp=[]
                tmp.append(key[0])
                tmp.append(key[1])
                output_lst.append(tmp.copy())
                k=k+1

    return output_lst

def main():
    
    intervals=[[1,3],[6,9]]
    newInterval=[2,5]
    print(LeetCode57(intervals,newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(LeetCode57(intervals, newInterval))

if __name__=='__main__':
    main()