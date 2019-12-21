'''
This problem was asked by Airbnb.
Given an array of integers, return the largest range, inclusive, of integers that are all included in the array.
For example, given the array [9, 6, 1, 3, 8, 10, 12, 11], return (8, 12) since 8, 9, 10, 11, and 12 are all in the array.
'''

def DailyCodingProblem393(ary):

    dict={}
    for key in ary:

        dict[key]=[]
        dict[key].append(key)
        cnt=key-1
        while cnt in ary:
            dict[key].append(cnt)
            cnt=cnt-1
    return sorted(dict.items(),key=lambda x:len(x[1]),reverse=True)[0][1]

def main():

    ary=[9, 6, 1, 3, 8, 10, 12, 11]
    print(DailyCodingProblem393(ary))

if __name__=='__main__':
    main()