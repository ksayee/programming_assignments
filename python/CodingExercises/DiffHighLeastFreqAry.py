# Difference between highest and least frequencies in an array
# Given an array, find the difference between highest occurrence and least occurrence of any number in an array

def DiffHighLeastFreqAry(ary):

    dict={}

    for key in ary:
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    max=0
    max_key=0
    min=999
    min_key=0

    for key,val in dict.items():
        if val>max:
            max=val
            max_key=key

        if val<min:
            min=val
            min_key=key

    return max_key-min_key

def main():

    ary=[7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
    print(DiffHighLeastFreqAry(ary))

    ary = [1, 1, 1, 3, 3, 3]
    print(DiffHighLeastFreqAry(ary))

if __name__=='__main__':
    main()