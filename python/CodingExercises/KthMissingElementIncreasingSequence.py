# k-th missing element in increasing sequence which is not present in a given sequence
# Given two sequences, one is increasing sequence a[] and another a normal sequence b[],
# find the K-th missing element in the increasing sequence which is not present in the given sequence.
# If no k-th missing element is there output -1

def KthMissingElementIncreasingSequence(ary1,ary2,k):

    fnl_lst=[]

    for key in ary1:
        if key not in ary2:
            fnl_lst.append(key)

    return fnl_lst[k-1]

def main():
    
    ary1=[0, 2, 4, 6, 8, 10, 12, 14, 15]
    ary2=[4, 10, 6, 8, 12]
    k=3
    print(KthMissingElementIncreasingSequence(ary1,ary2,k))

if __name__=='__main__':
    main()