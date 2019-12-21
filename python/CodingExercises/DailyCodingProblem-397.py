'''
This problem was asked by Microsoft.
You are given a list of jobs to be done, where each job is represented by a start time and end time.
Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.
For example, given the following jobs (there is no guarantee that jobs will be sorted):
[(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
Return:
[(1, 4),
(4, 7),
(8, 11)]
'''

def DailyCodingProblem397(ary):

    sort_list=sorted(ary,key=lambda x:x[0])
    dict={}
    for tup in sort_list:
        flg=False
        for key,val in dict.items():
            if tup[0]>=val[-1][1]:
                dict[key].append(tup)
                flg=True
        if flg==False:
            dict[tup[1]]=[]
            dict[tup[1]].append(tup)
    return sorted(dict.items(),key=lambda x:len(x[1]),reverse=True)[0][1]

def main():

    ary=[(0, 6),(1, 4),(3, 5),(3, 8),(4, 7),(5, 9),(6, 10),(8, 11)]
    print(DailyCodingProblem397(ary))

if __name__=='__main__':
    main()