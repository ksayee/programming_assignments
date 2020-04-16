'''
This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

def DailyCodingProblem514(ary):

    dict={}

    for element in ary:
        tmp=[]
        tmp.append(element)
        key=element+1
        while key in ary:
            tmp.append(key)
            key=key+1
        key=element-1
        while key in ary:
            tmp.append(key)
            key=key-1
        if tuple(sorted(tmp)) not in dict.keys():
            dict[tuple(sorted(tmp))]=len(tmp)

    return sorted(dict.items(),key=lambda x:x[1],reverse=True)[0][0]

def main():

    ary=[100, 4, 200, 1, 3, 2]
    print(DailyCodingProblem514(ary))

if __name__=='__main__':
    main()