'''
This problem was asked by Twitter.
Given a string, sort it in decreasing order based on the frequency of characters.
If there are multiple possible solutions, return any of them.
For example, given the string tweet, return tteew. eettw would also be acceptable.
'''

import collections
def DailyCodingProblem386(str1):

    dict=collections.Counter(str1)

    sort_dict=sorted(dict.items(),key=lambda x:x[1])

    output_list=[]
    for tup in sort_dict:
        cnt=tup[1]
        while cnt>0:
            output_list.append(tup[0])
            cnt=cnt-1
    return ''.join(output_list)

def main():

    str1='tweet'
    print(DailyCodingProblem386(str1))

if __name__=='__main__':
    main()