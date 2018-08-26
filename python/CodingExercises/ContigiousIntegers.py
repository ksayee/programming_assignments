# Check if array contains contiguous integers with duplicates allowed
# Given an array of n integers(duplicates allowed).
# Print “Yes” if it is a set of contiguous integers else print “No”.

def ContigousIntegers(ary):

    lst=sorted(set(ary))

    flg=True
    for i in range(1,len(lst)):

        if lst[i]-lst[i-1]>1:
            flg=False
            break

    if flg==True:
        return "Yes"
    else:
        return "No"

def main():
    
    ary=[5, 2, 3, 6, 4, 4, 6, 6]
    print(ContigousIntegers(ary))

    ary = [10, 14, 10, 12, 12, 13, 15]
    print(ContigousIntegers(ary))

if __name__=='__main__':
    main()