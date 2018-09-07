# Pair with given product | Set 1 (Find if any pair exists)
# Given an array of distinct elements and a number x,
# find if there is a pair with product equal to x.

def PairGivenProduct(ary,k):

    dict={}

    fnl_lst=[]
    for key in ary:

        if key!=0:
            num=int(k/key)
            if num in dict.keys():
                tup=(key,num)
                fnl_lst.append(tup)
            else:
                dict[key]=1
        else:
            dict[key]=1

    if len(fnl_lst)==0:
        return -1
    else:
        return fnl_lst

def main():
    
    ary=[10, 20, 9, 40]
    k=400
    print(PairGivenProduct(ary,k))

    ary = [10, 20, 9, 40]
    k = 190
    print(PairGivenProduct(ary, k))

    ary = [-10, 20, 9, -40]
    k = 400
    print(PairGivenProduct(ary, k))

    ary = [-10, 20, 9, 40]
    k = -400
    print(PairGivenProduct(ary, k))

    ary = [0, 20, 9, 40]
    k = 0
    print(PairGivenProduct(ary, k))

if __name__=='__main__':
    main()