# Union and Intersection of 2 List

def UnionIntersectionList(ary1,ary2):

    un_lst=[]
    int_lst=[]

    for l in ary1:
        if l not in un_lst:
            un_lst.append(l)

    for l in ary1:
        if l in ary2:
            int_lst.append(l)

    print("Union List: ", un_lst)
    print("Intersection List:", int_lst)

def main():
    
    ary1=[10,15,4,20]
    ary2=[8,4,2,10]
    UnionIntersectionList(ary1,ary2)

if __name__=='__main__':
    main()