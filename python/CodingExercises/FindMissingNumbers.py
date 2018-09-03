# Find All the missing numbers

def FindMissingNumbers(ary):

    fnl_lst=[]
    ary.sort()

    for i in range(1,len(ary)):

        if ary[i]-ary[i-1]>1:
            tmp=ary[i]-1
            while tmp>ary[i-1]:
                fnl_lst.append(tmp)
                tmp=tmp-1

    fnl_lst.sort()

    return fnl_lst

def main():

    ary=[2, 5, 6, 3, 9]
    print(FindMissingNumbers(ary))

    ary = [1, 7, 3, 13, 5, 10, 8, 4, 9]
    print(FindMissingNumbers(ary))

    ary = [10, 13, 14, 15, 18, 22, 30, 31, 32]
    print(FindMissingNumbers(ary))

if __name__=='__main__':
    main()