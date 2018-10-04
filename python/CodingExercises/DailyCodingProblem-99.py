'''

This problem was asked by Microsoft.
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.
'''

def DailyCodingProblem99(ary):

    cnt=0
    max_cnt=0

    dict={}

    for key in ary:
        if key not in dict.keys():
            dict[key]=1

    for key in ary:
        cnt=0
        while key in dict.keys():
            key=key+1
            cnt=cnt+1

        if cnt>max_cnt:
            max_cnt=cnt

    return max_cnt

def main():

    ary=[100, 4, 200, 1, 3, 2]
    print(DailyCodingProblem99(ary))

if __name__=='__main__':
    main()