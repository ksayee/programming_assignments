'''
Given an arrary of uniquite non-negative integers and a positive number K, write a funcation to find all pairs of numbers in the array that sum to X.
'''

def ExpediaSDE1Problem2(ary,k):

    dict={}

    fnl_lst=[]
    for key in ary:

        diff=k-key
        if diff in dict.keys():
            tup=(diff,key)
            if sorted(tup) not in fnl_lst:
                fnl_lst.append(sorted(tup))
        else:
            if key not in dict.keys():
                dict[key]=1
    return fnl_lst

def main():

    ary=[2,8,9,5,3,87,4,6,33,1]
    k=7
    print(ExpediaSDE1Problem2(ary,k))

if __name__=='__main__':
    main()