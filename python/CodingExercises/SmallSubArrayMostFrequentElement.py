# Smallest subarray with all occurrences of a most frequent element
# Given an array, A.Let x be an element in the array.x has the maximum frequency in the array.
# Find the smallest subsegment of the array which also has x as the maximum frequency element.

def SmallSubArrayMostFrequentElement(ary):

    dict={}

    for i in range(0,len(ary)):
        key=ary[i]

        if key in dict.keys():
            dict[key].append(i)
        else:
            tmp=[]
            tmp.append(i)
            dict[key]=tmp

    max=0

    for key,val in dict.items():
        if len(val)>max:
            max=len(val)

    fnl_lst=[]

    for key,val in dict.items():
        if len(val)==max:
            tup=(key,val[len(val)-1]-val[0])
            fnl_lst.append(tup)

    sort_lst=sorted(fnl_lst,key=lambda x:x[1])[0]

    idx1=dict[sort_lst[0]][0]
    idx2 = dict[sort_lst[0]][len(dict[sort_lst[0]])-1]

    return ary[idx1:idx2+1]

def main():
    
    ary=[4, 1, 1, 2, 2, 1, 3, 4,3,4]
    print(SmallSubArrayMostFrequentElement(ary))

    ary = [1, 2, 2, 3, 1]
    print(SmallSubArrayMostFrequentElement(ary))

if __name__=='__main__':
    main()