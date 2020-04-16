'''
Merge overlapping intervals. See below for example:
[1,3] [2,5] [8,9] => [1,5] [8,9]
[1,3] [2,6] [4,99] => [1,99]
'''

def MergeOverlappingIntervals(intervals):

    sort_lst=sorted(intervals,key=lambda x:x[0])

    output_lst=[]
    output_lst.append(sort_lst[0])
    k=0
    for i in range(1,len(sort_lst)):
        key=sort_lst[i]
        if key[0]<output_lst[k][1]:
            if key[1]<output_lst[k][1]:
                pass
            else:
                tup=[output_lst[k][0],key[1]]
                del output_lst[k]
                output_lst.append(tup.copy())
        else:
            output_lst.append(key.copy())
            k=k+1
    return output_lst

def main():

    intervals=[[1,3],[2,5],[8,9]]
    print(MergeOverlappingIntervals(intervals))

    intervals = [[1,3],[2,6],[4,99]]
    print(MergeOverlappingIntervals(intervals))

if __name__=='__main__':
    main()