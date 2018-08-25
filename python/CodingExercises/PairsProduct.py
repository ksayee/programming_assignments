# Count pairs whose products exist in array
# Given an array, count those pair whose product value is present in array.

def PairsProduct(ary):

    dict={}

    for l in ary:
        if l in dict.keys():
            continue
        else:
            dict[l]=1

    fnl_lst=[]
    for i in range(0,len(ary)):
        for j in range(i,len(ary)):
            prd=ary[i]*ary[j]

            if prd in dict.keys():
                tup=(ary[i],ary[j])
                fnl_lst.append(tup)

    return fnl_lst
    
def main():
    
    ary=[6, 2, 4, 12, 5, 3]
    print(PairsProduct(ary))

    ary = [3, 5, 2, 4, 15, 8]
    print(PairsProduct(ary))

if __name__=='__main__':
    main()