# How to check if two given sets are disjoint?
# Given two sets represented by two arrays,
# how to check if the given two sets are disjoint or not? It may be assumed that the given arrays have no duplicates.

def DisjointSets(ary1,ary2):

    flg=True

    for key in ary1:
        if key in ary2:
            flg=False
            break

    if flg==True:
        for key in ary2:
            if key in ary1:
                flg=False
                break

    if flg==True:
        return "Yes"
    else:
        return "No"

def main():
    
    ary1=[12, 34, 11, 9, 3]
    ary2 = [2, 1, 3, 5]
    print(DisjointSets(ary1,ary2))

    ary1 = [12, 34, 11, 9, 3]
    ary2 = [7, 2, 1, 5]
    print(DisjointSets(ary1, ary2))

if __name__=='__main__':
    main()